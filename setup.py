# from setuptools import setup, find_packages
from importlib_metadata import entry_points
import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='n',
    version = '0.0.1',
    author = 'wbwqq',
    description= 'A cli notetaking tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/wbwqq/n',
    project_urls = {
        "Bug Tracker" : 'https://github.com/wbwqq/n/issues',
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    package_dir={'':'n'},
    py_modules=['n'],
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'n = n.n'
        ]
    }
)