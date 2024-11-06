from setuptools import setup

APP = ['main.py'] 
DATA_FILES = ['DB/tattoo_world.db'] 
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)