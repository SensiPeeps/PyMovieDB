from setuptools import setup, find_packages
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pymoviedb',
    description='A simple wrapper over themoviedb.org API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/starry69/PyMovieDB',
    author='Stɑrry Shivɑm',
    author_email='starry369126@outlook.com',
    version='1.2',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.6',
    keywords='api development tmdb themoviedb wrapper library python3',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ])
