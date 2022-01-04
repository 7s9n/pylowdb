from setuptools import(
    setup,
    find_packages,
)
import os


def read_file(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


setup(
    name='Pylowdb',
    version='1.0.2',
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author='Hussein Sarea',

    author_email='zzzsssx0@gmail.com',

    description='Tiny local JSON database for Python, django, flask',

    long_description=read_file('README.md'),

    long_description_content_type='text/markdown',

    url='https://github.com/Ho011/pylowdb',

    keywords=[
        "database",
        "db",
        "electron",
        "embed",
        "embedded",
        "flat",
        "JSON",
        "local",
        "localStorage",
    ],
    license='MIT',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],

    install_requires=['PyYAML'],

    project_urls={ 
        'Bug Reports': 'https://github.com/Ho011/pylowdb/issues',
        'Funding': 'https://www.buymeacoffee.com/HusseinSarea',
        'Source': 'https://github.com/Ho011/pylowdb',
    },
)
