# FastAPI Chinook Database API

This project is a simple API that provides access to a SQLite database using FastAPI. It allows users to query the Chinook database (available at https://www.sqlitetutorial.net/sqlite-sample-database/) for information about artists, albums, and tracks.

## Features

- Search for artists by name and display artists with the given name.
- Search for albums by artist ID and display the corresponding album names.
- Search for tracks by album ID and display the corresponding track names.

## Project Structure

The project is organized as follows:

- `api.py`: Contains the FastAPI application and defines the routes.
- `database.py`: Provides utility functions for database access using SQLAlchemy.
- `models.py`: Defines SQLAlchemy models for the Chinook database tables.
- `client.py`: A script for interacting with the API and displaying results.
- `test.py`: Unit tests for the API endpoints.
- `requirements.txt`: Lists the required packages for the project.