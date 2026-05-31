# pybuilder

A minimal Python CLI tool with CI/CD.

## Usage

```bash
python main.py greet Alice
python main.py add 3 7
```

## Run tests

```bash
pip install -r requirements.txt
pytest
```

## Docker

```bash
docker build -t pybuilder .
docker run pybuilder greet World
```
