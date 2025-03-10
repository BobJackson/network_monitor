from setuptools import setup

APP = ['network_speed.py']
DATA_FILES = []
ICON_PATH = 'network_speed.icns'
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile': ICON_PATH,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
