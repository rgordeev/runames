import runames
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as changes_file:
    changes = changes_file.read()

with open('CONTRIBUTING.rst') as contributing_file:
    contributing = contributing_file.read()


setup(
    name=runames.__title__,
    version=runames.__version__,
    author=runames.__author__,
    url="https://github.com/treyhunner/names",
    description="Generate random names",
    long_description='\n\n'.join((
        readme,
        changes,
        contributing,
    )),
    license=runames.__license__,
    packages=find_packages(),
    package_data={'runames': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'runames = runames.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='test_names',
)
