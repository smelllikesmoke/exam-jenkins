# Flask Application for Jenkins Pipeline Testing

A simple Flask application designed for testing Jenkins CI/CD pipelines.

## Overview

This repository contains a minimal Flask application with dummy endpoints, pytest tests, and a Jenkinsfile for automated build, test, and deployment.

## Application Endpoints

- `GET /` - Welcome/home endpoint
- `GET /health` - Health check endpoint
- `GET /api/data` - Simple API endpoint returning dummy JSON data

## Setup

### Prerequisites

- Python 3.x
- pip

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/smelllikesmoke/exam-jenkins.git
cd exam-jenkins
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

```bash
pytest tests/ -v
```

Or with coverage:
```bash
pytest tests/ -v --cov=app
```

## Jenkins Pipeline

The repository includes a `Jenkinsfile` that defines a CI/CD pipeline with the following stages:

1. **Checkout** - Clone the repository
2. **Install Dependencies** - Install Python packages
3. **Test** - Run pytest tests
4. **Build** - Prepare application for deployment
5. **Deploy** - Copy files to deployment directory

## Project Structure

```
exam/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── tests/
│   └── test_app.py       # Pytest test cases
├── Jenkinsfile           # Jenkins pipeline definition
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## License

This is a test/dummy application for educational purposes.

