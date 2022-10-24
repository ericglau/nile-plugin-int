### Installation

1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Clone this project.
4. From this project's root, setup venv and install dependencies:
```
python3 -m venv env
source env/bin/activate
poetry install
pip3 install -e .
```

### Testing

`poetry run pytest tests`

### Running manually

`nile run tests/resources/scripts/script.py`
