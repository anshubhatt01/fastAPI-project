# fastAPI-project

A simple FastAPI application demonstrating basic API setup and routing.

## Project Structure

```
fastAPI-project/
├── main.py              # Main FastAPI application with root endpoint
├── requirements.txt     # Project dependencies
├── README.md           # This file
└── .venv/              # Virtual environment (not included in version control)
```

## Features

- Simple FastAPI application
- Root endpoint (`GET /`) that returns a greeting message

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd fastAPI-project
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

- **GET /** - Returns a greeting message
  - Response: `{"Hello": "World from fastapi!"}`

## API Documentation

Once the server is running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
