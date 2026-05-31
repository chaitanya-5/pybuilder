# pybuilder

A minimal Python CLI tool with CI/CD pipeline using GitHub Actions and Docker.

## What this project does

- Simple Python CLI with `greet` and `add` commands
- Automated CI/CD via GitHub Actions on every push
- Docker image build to verify containerization

## CI/CD Pipeline

Every push to `main` triggers two jobs:

| Job | What it does |
|-----|-------------|
| **test** | Installs dependencies and runs pytest |
| **docker** | Builds the Docker image after tests pass |

> The Docker image is built but not pushed. To push to a registry, a Docker Hub secret needs to be configured.

## Usage

### Run locally

```bash
python main.py greet Alice
# Hello, Alice!

python main.py add 3 7
# 10.0
```

### Run with Docker

```bash
docker build -t pybuilder .
docker run pybuilder greet World
docker run pybuilder add 5 10
```

### Run tests

```bash
pip install -r requirements.txt
pytest
```

## Project Structure

```
pybuilder/
├── main.py                      # CLI app
├── test_main.py                 # pytest tests
├── Dockerfile                   # Docker build
├── requirements.txt             # Dependencies
└── .github/
    └── workflows/
        └── ci.yml               # GitHub Actions pipeline
```

## Status

![CI](https://github.com/chaitanya-5/pybuilder/actions/workflows/ci.yml/badge.svg)
