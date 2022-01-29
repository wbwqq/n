# from setuptools import setup, find_packages
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
    url = 'https://github.com/wbwqq/miniparser',
    project_urls = {
        "Bug Tracker" : 'https://github.com/wbwqq/miniparser/issues',
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'':'miniparser'},
    py_modules=['miniparser'],
    python_requires=">=3.6",
)