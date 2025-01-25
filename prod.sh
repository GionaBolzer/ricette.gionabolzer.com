#!/bin/bash
source venv/bin/activate
pip install pyproject.toml
python -m build --wheel
scp dist/ricette_gionabolzer_com-1.0.0-py2.py3-none-any.whl root@192.168.0.118:~/ricette.gionabolzer.com/
ssh root@192.168.0.118 'systemctl stop ricette;source ~/ricette.gionabolzer.com/venv/bin/activate;pip install --force-reinstall ~/ricette.gionabolzer.com/ricette_gionabolzer_com-1.0.0-py2.py3-none-any.whl;systemctl start ricette'