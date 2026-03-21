# Complaint Backend

A FastAPI-based backend service for managing complaints.

## Project Structure

- `main.py`: FastAPI application entry point with routes
- `database/`: Database configuration and connection
- `models/`: SQLAlchemy database models and Pydantic schemas
- `services/`: Business logic services

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Open http://127.0.0.1:8000/docs for the interactive API documentation.

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check
- `GET /complaints`: Get all complaints
- `GET /complaints/{id}`: Get complaint by ID
- `POST /complaints`: Create a new complaint
- `PUT /complaints/{id}`: Update complaint status
- `DELETE /complaints/{id}`: Delete a complaint

## Database

Uses SQLite database (`complaints.db`) for simplicity. Tables are created automatically on startup.