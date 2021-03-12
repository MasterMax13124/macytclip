#!/bin/bash

python3 -m venv macytclip
source macytclip/bin/activate
pip install py2app klaxon clipboard rumps youtube-dl
python3 setup.py py2app
deactivate
mv dist/macytclip.app macytclip.app
rm -rf dist
rm -rf build
