runames
=====

.. image:: https://travis-ci.org/rgordeev/runames.svg?branch=master
   :target: http://travis-ci.org/rgordeev/runames

Random russians names generator


Installation
------------

Download from github and put runames directory into your root project folder.
And then use import expression.

Usage
-----

RuNames can be used as a command line utility or imported as a Python package.

Command Line Usage
~~~~~~~~~~~~~~~~~~
To use the script from the command line:

.. code-block:: bash

    $ runames
    Иван Бирнштейн

Python Package Usage
~~~~~~~~~~~~~~~~~~~~
Here are examples of all current features:

.. code-block:: pycon

    >>> import runames
    >>> runames.get_full_name()
    u'Иван Иванов'
    >>> runames.get_full_name(gender='male')
    u'Иван Петров'
    >>> runames.get_first_name()
    'Иван'
    >>> runames.get_first_name(gender='female')
    'Алена'
    >>> runames.get_last_name()
    'Елена'


License
-------

This project is released under an `MIT License`_.

Data in the following files are public domain (derived from myData.biz data):

- dist.female.ru.last
- dist.male.ru.last
- dist.female.ru.first
- dist.male.ru.first

.. _mit license: http://th.mit-license.org/2013
