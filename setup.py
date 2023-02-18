"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['YouTube2MP4Downloader.py']
DATA_FILES = []
OPTIONS = {
    "packages": ["tkinter", "yt_dlp"]
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
