# -*- coding: utf-8 -*-
"""
Pygments plugin
"""
from setuptools import setup

__author__ = 'Peter Vizi'

setup(
    name='NesC',
    version='0.1',
    description=__doc__,
    author=__author__,
    packages=['lexer'],
    entry_points='''
    [pygments.lexers]
    nesclexer = lexer:NesCLexer
    '''
)
