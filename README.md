# Purewater API

The Purewater API is a backend application built using Flask to help manage users login and register

## Features

- **User Management**: Register, log in, update, and delete users.
- **Authentication**: Uses JWT for user authentication.

## Technologies Used

- Flask as the web application framework.
- Flask-SQLAlchemy as the ORM.
- Flask-JWT-Extended for JWT-based authentication.
- MySQL as the database management system.

## Deployment

The application is deployed on Heroku and can be accessed [here](https://revou-final-project-be-group-d-production.up.railway.app/).

## Environment Setup

Ensure you have Python and pip installed. You also need to have MySQL set up and running.

## Installation

- Clone this repository.

```bash
   git https://github.com/isnendyankp/RevoU-Final-Project-BE-Group-D.git
```

- Install dependencies using pip

```bash
   pip install -r requirements.txtl
```

- Create a `.env` file at the root of the project and configure the environment variables (DB_URI, JWT_SECRET_KEY, etc.).

- Run the application.



```bash
   1. source .venv/Scripts/activate (Windows)
   2. python main.py
```

## Usage

## API Documentation

For more detailed information on API endpoints and their usage, please refer to our [API Documentation](https://documenter.getpostman.com/view/32137747/2sA3JJ9ia5).

### Registering a New User

```bash
POST /register
{
"username": "newuser",
"email": "newuser@example.com",
"password": "strongpassword"
}
```

### Login User

```bash
POST /login
{
"username": "newuser",
"password": "strongpassword"
}
```



