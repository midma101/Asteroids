from __future__ import with_statement, print_function
import os
from fabric.api import local, lcd, prefix
from fabric.colors import red, cyan

BASE_DIR = os.getcwd()

APP_DIR = '/'.join((BASE_DIR, 'version1'))

PYGLET_ENV_DIR = '/Users/midma101/envs/pyglet_env'

PYGLET_ENV_ACTIVATE = 'source ' + '/'.join((PYGLET_ENV_DIR, 'bin', 'activate'))

WEB_BRANCH = 'master'

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))


def start():
    """Starts the app"""
    with lcd(APP_DIR):
        with prefix(PYGLET_ENV_ACTIVATE):
            print(red("Firing up the app!!!"))
            local('pythonw app.py')