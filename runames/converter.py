from __future__ import unicode_literals

import codecs
import json
from os.path import abspath, join, dirname
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender


full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'first:male': full_path('russian_names.json'),
    'first:female': full_path('russian_names.json'),
    'last': full_path('russian_surnames.json'),
}


class Converter(object):
    def __init__(self, names_src = 'russian_names.json', lastnames_src = 'russian_surnames.json'):
        self.names_scr = names_src
        self.lastnames_src = lastnames_src

    def convert_names(self):
        json_data = json.load(codecs.open(self.names_scr, 'r', 'utf-8-sig'))
        if json_data is not None:
            for item in json_data:
                if item['PeoplesCount'] > 0 and item['PeoplesCount'] < 1000:
                    data = {
                        "id": item["ID"],
                        "name": item["Name"],
                        "gender": "male" if item["Sex"] == 'М' else "female",
                        "count": item["PeoplesCount"]
                    }
                    file_name = "male_russian_names.txt" if item["Sex"] == 'М' else "female_russian_names.txt"
                    self.dump_results(data, full_path(file_name))

    def convert_lastnames(self):
        json_data = json.load(codecs.open(self.lastnames_src, 'r', 'utf-8-sig'))
        p = Petrovich()

        for item in json_data:
            if item['PeoplesCount'] > 0 and item["PeoplesCount"] < 1000:
                m_data = {
                    "id": item["ID"],
                    "name": item["Surname"],
                    "gender": item["Sex"],
                    "count": item["PeoplesCount"]
                }
                f_data = {
                    "id": item["ID"],
                    "name": p.lastname(item["Surname"], Case.GENITIVE, Gender.MALE),
                    "gender": item["Sex"],
                    "count": item["PeoplesCount"]
                }
                m_file = "male_russian_lastnames.txt"
                f_file = "female_russian_lastnames.txt"
                self.dump_results(m_data, full_path(m_file))
                self.dump_results(f_data, full_path(f_file))

    def sort_names(self, file_name):
        names = []
        with open(file_name, 'r', encoding='utf-8') as names_file:
            for item in names_file:
                name = json.loads(item)
                names.append(name)
        names.sort(key = lambda name: name["count"])
        return names

    def sort_data(self, file_name):
        names = self.sort_names(file_name)
        with open(file_name, 'w', encoding='utf-8') as data_file:
            for name in names:
                data_file.write(json.dumps(name))
                data_file.write('\n')


    def dump_results(self, data, file_name):
        with open(file_name, 'a', encoding='utf-8') as dump_file:
            dump_file.write(json.dumps(data))
            dump_file.write('\n')


if __name__ == '__main__':
    c = Converter()
    #c.convert_names()
    #c.convert_lastnames()
    #print(c.sort_names('male_russian_names.txt'))
    c.sort_data('male_russian_names.txt')
    c.sort_data('female_russian_names.txt')
    c.sort_data('female_russian_lastnames.txt')
    c.sort_data('male_russian_lastnames.txt')
