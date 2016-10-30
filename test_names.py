#!/usr/bin/env python
import unittest
import sys
from os.path import abspath, join, dirname
try:
    from StringIO import StringIO
except:
    from io import StringIO
from collections import defaultdict
import runames
from runames.main import main


full_path = lambda filename: abspath(join(dirname(__file__), filename))


class patch_stdout(object):
    def __init__(self):
        self.stdout = StringIO()
        self.real_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = self.stdout
        return sys.stdout

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self.real_stdout


class patch_file:

    def __init__(self, file_dict):
        self.files = file_dict

    def __enter__(self):
        self.old_files = runames.FILES
        runames.FILES = self.files

    def __exit__(self, type, value, traceback):
        runames.FILES = self.old_files

test_files = {
    'first:male': full_path('test/male.txt'),
    'first:female': full_path('test/female.txt'),
    'last:male': full_path('test/last.txt'),
    'last:female': full_path('test/last.txt')
}


class NamesTest(unittest.TestCase):

    def test_random_gender(self):
        counts = defaultdict(int)
        rounds = 5000.0
        with patch_file(test_files):
            for i in range(int(rounds)):
                runames.get_first_name()
                counts[runames.get_first_name()] += 1
        self.assertAlmostEqual(counts['Male'] / rounds, 0.500, delta=0.05)
        self.assertAlmostEqual(counts['Female'] / rounds, 0.500, delta=0.05)

    def test_correct_files(self):
        with patch_file(test_files):
            self.assertEqual(runames.get_first_name(gender='male'), "Male")
            self.assertEqual(runames.get_first_name(gender='female'), "Female")
            self.assertEqual(runames.get_last_name(gender='female'), "Last")
            self.assertEqual(runames.get_last_name(gender='male'), "Last")

    def test_empty_file(self):
        empty_files = {
            'first:male': full_path('test/empty.txt'),
            'first:female': full_path('test/empty.txt'),
            'last:male': full_path('test/empty.txt'),
            'last:female': full_path('test/empty.txt'),
        }
        with patch_file(empty_files):
            self.assertEqual(runames.get_first_name(gender='male'), "")
            self.assertEqual(runames.get_first_name(gender='female'), "")
            self.assertEqual(runames.get_last_name(gender='female'), "")
            self.assertEqual(runames.get_last_name(gender='male'), "")

    def test_only_male_and_female_gender_are_supported(self):
        with self.assertRaises(ValueError):
            runames.get_first_name(gender='other')


class CommandLineTest(unittest.TestCase):

    def test_cli(self):
        with patch_stdout() as stdout:
            with patch_file(test_files):
                main()
                self.assertIn(stdout.getvalue(),
                              ["Male Last\n", "Female Last\n"])


if __name__ == '__main__':
    unittest.main()
