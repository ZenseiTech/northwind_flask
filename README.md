**Build the requirements**:

Create virtual environment

    python3.10 -m venv .venv

    source ./.venv/bin/activate

Read: https://pypi.org/project/pip-tools/

    python -m pip install pip-tools

**Build the requirements**

    pip-compile setup.cfg

    pip-sync requirements.txt

**Build the local requirements**:

    pip-compile requirements_local.in

    pip-sync requirements_local.txt

**Commit hooks**

https://pre-commit.com/

    pip install pre-commit

    Run:

        pre-commit install

        Make sure you have created a git branch before running below command and make sure the existance of file:

            .pre-commit-config.yaml

        pre-commit run --all-files
