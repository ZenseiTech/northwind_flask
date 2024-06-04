**Build the requirements**:

Create virtual environment

    python3.10 -m venv .venv

    source ./.venv/bin/activate

Read: https://pypi.org/project/pip-tools/

    python -m pip install pip-tools

    pip-compile setup.cfg

    pip-sync requirements.txt

**Build the local requirements**:

    pip-compile requirements_local.in

    pip-sync requirements_local.txt
