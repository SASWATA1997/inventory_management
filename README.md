# Inventory Management REST API

A step-by-step guide to setting up and using the Inventory Management REST API built with Django and Django REST Framework.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [startServer](#Start-server)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Introduction

This project is a RESTful API for managing inventory items, including features such as user authentication using JSON Web Tokens (JWT). It allows you to create, retrieve, update, and delete inventory items securely.

## Features

- User authentication with JWT.
- CRUD operations for inventory items.
- Secure access to APIs.
- Lightweight and fast.

## Technologies Used

- **Django**: The web framework used for building the API.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **PostgreSQL / MySQL / SQLite**: Database options for storing user and item data.
- **Simple JWT**: For handling JSON Web Tokens for authentication.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.8 or later**
- **pip** (Python package installer)
- **Virtualenv** (recommended for managing Python packages)

## Installation

Follow these steps to set up the project on your local machine.

### Step 1: Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/yourusername/inventory_management_rest.git
cd inventory_management_rest
```
### Step 2: Create a Virtual Environment
```bash
python -m venv env  # Create a virtual environment

pip install -r requirements.txt
```
### Step 3: Activate the Virtual Environment
Activate the virtual environment with the following command:
```bash
env\Scripts\activate
```
### Step 4: Install Required Packages
Install the project dependencies using pip:
```bash
pip install -r requirements.txt
```
### Step 5: Apply Migrations
```bash
python manage.py makemigrations:
```
```bash
python manage.py migrate
```
## Start server
To start the development server:
```bash
python manage.py runserver
```
## API Endpoints
Here are the available API endpoints:

 Method	Endpoint	Description
1. POST	/api/token/	Obtain JWT token.
2. POST	/api/items/	Create a new item.
3. GET	/api/items/	Retrieve a list of items.
4. GET	/api/items/<int:id>/	Retrieve a specific item by ID.
5. PUT	/api/items/<int:id>/	Update a specific item by ID.
6. DELETE	/api/items/<int:id>/	Delete a specific item by ID.

### example of Obtaining a Token
Use a tool like Postman or cURL to obtain a JWT token.

## Using Postman:

1. Set the request method to POST.
2. Enter the URL: http://localhost:8000/api/token/.
3. In the Body tab, select raw and set the type to JSON.
4. Enter the following JSON payload:
{
    "username": "Saswata",
    "password": "1234"
}
5. Send the request and receive a JWT token in the response.
## Testing
To run the tests for this project, use the following command:
```bash
python manage.py test
```

