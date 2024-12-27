# Project-management
This is a Django-based project management system that includes user registration, login, project management, task tracking, and commenting functionality. It uses Django REST Framework to expose APIs and includes JWT authentication.

## Prerequisites
Ensure that the following software is installed on your local machine:
1. Python 3.12+
2. pip (Python package installer)
3. PostgreSQL or SQLite (depending on your setup)

## Setup Instructions
1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/hachibkhan19/project-management.git
cd project-management

```
2. Install Dependencies

Install dependencies using Pipenv:
```
pip install pipenv
pipenv install

```
This will install the required packages, including:

* django: A high-level Python web framework.
* djangorestframework: A powerful toolkit for building Web APIs.
* djangorestframework-simplejwt: A simple JWT authentication system for Django REST Framework.
* drf-yasg: A great tool for generating real Swagger/OpenAPI 2.0 specifications for your Django REST API.

3. Set Up the Database
* If you’re using SQLite (default), no additional configuration is required.

4. Migrate the Database

Run the database migrations to create the necessary tables:
```
python manage.py makemigrations
python manage.py migrate

```

5. Create a Superuser (Optional)

To create a superuser for accessing the Django admin panel, run:
```
python manage.py createsuperuser
```
6. Run the Development Server

Start the Django development server:
```
python manage.py runserver
```
Your application will be running at http://127.0.0.1:8000/.

7. Swagger Documentation

Navigate to http://127.0.0.1:8000/swagger/ to view the interactive API documentation.

8. Access the API
The API endpoints are available at:

* `User Registration`: POST /api/users/register/
* `User Login`: POST /api/users/login/
* `User CRUD Operations`:
* GET /api/users/: List all users.
* POST /api/users/: Register a new user.
* PUT /api/users/{id}/: Update user details.
* DELETE /api/users/{id}/: Delete a user account.
* `Project Management`:
* GET /api/projects/: List all projects.
* POST /api/projects/: Create a new project.
* PUT /api/projects/{id}/: Update project details.
* DELETE /api/projects/{id}/: Delete a project.
`Task Management`:
* GET /api/projects/{project_id}/tasks/: List all tasks for a project.
* POST /api/projects/{project_id}/tasks/: Create a new task under a project.
* `Comment Management`:
* GET /api/tasks/{task_id}/comments/: List all comments for a task.
* POST /api/tasks/{task_id}/comments/: Add a comment to a task.
