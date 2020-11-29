#!/usr/bin/bash
# USAGE: bash scripts/install_python_packages.sh

set -ex

cd scripts
pip install pip-tools
pip-compile requirements.in
pip-sync

pip install torch==1.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

cd ../ILYS-aoba-chatbot/fairseq
pip install --editable .
