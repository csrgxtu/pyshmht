#!/usr/bin/python
import os
from distutils.core import setup, Extension
from setuptools import setup, Extension
shmht = Extension('shmht',
    sources = ['shmht.c', 'hashtable.c'],
    extra_compile_args = '-g3 -Wall -Werror -O3 -march=native'.split(),
)

setup(
    name            = 'pyshmht3',
    version         = '0.0.1',
    author          = 'minyakonga,felix021',
    author_email    = 'minyakonga@gmail.com',
    description     = 'provide sharing memory based hash table for python, one process write, others read',
    license         = "BSD",
    keywords        = "python extension sharing memory based hash table",
    url             = "http://github.com/csrgxtu/pyshmht",
    ext_modules     = [shmht],
    packages        = ["pyshmht3"]
)
