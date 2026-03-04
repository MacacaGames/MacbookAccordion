from setuptools import setup

APP = ['lid_accordion.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame', 'numpy', 'pybooklid', 'sounddevice'],
    'includes': ['sounddevice'],
    'plist': {
        'CFBundleName': 'LidAccordion',
        'CFBundleDisplayName': 'LidAccordion',
        'CFBundleIdentifier': 'games.macaca.lidaccordion',
        'CFBundleShortVersionString': '0.0.1',
        'CFBundleVersion': '0.0.1',
        'NSHighResolutionCapable': True,
    },
}
setup(app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS}, setup_requires=['py2app'])
