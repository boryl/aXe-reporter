'''
    File name: config.py
    Project: aXe reporter
    Author: Björn-Olle Rylander
    Date created: 2019-07-07
    Python Version: 3.7.4
    Description: Configuration
'''

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base config vars."""
    SECRET_KEY = 'secret'
    FLASK_ENV = 'development'
    AXE_PATH = basedir + "/axe/"


class development(Config):
    DEBUG = True
    TESTING = True
    