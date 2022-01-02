echo "############# START ###################"
wget -O -  https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
rm -rf poetry.lock
poetry install --no-dev --no-root
poetry build
pip install --no-deps dist/*.whl
echo "############# END ###################"
