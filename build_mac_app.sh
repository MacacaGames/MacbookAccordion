#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -U pip wheel
python -m pip install py2app pygame numpy pybooklid sounddevice

rm -rf build dist
python setup.py py2app

echo "Done: dist/LidAccordion.app"
echo "Run:"
echo "  ./dist/LidAccordion.app/Contents/MacOS/LidAccordion"
