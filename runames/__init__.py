from __future__ import unicode_literals
from os.path import abspath, join, dirname
import json
import random


__title__ = 'runames'
__version__ = '0.1'
__author__ = 'Roman Gordeev'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.ru.first'),
    'first:female': full_path('dist.female.ru.first'),
    'last:male': full_path('dist.male.ru.last'),
    'last:female': full_path('dist.female.ru.last'),
}


def get_name(filename):
    with open(filename) as file:
        lines = list(file)
        if lines is not None and lines and len(lines) != 0:
            data = json.loads(random.choice(lines))
            return data["name"]
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['last:%s' % gender]).capitalize()


def get_full_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return "{0} {1}".format(get_first_name(gender), get_last_name(gender))
