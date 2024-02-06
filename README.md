# Admin Panel Registration Project

This project is a simple Django web application for user registration with an admin panel.

## Features

- User registration with username, email, and password
- Admin panel for managing user registrations
- Password hashing for enhanced security
- Bootstrap for a responsive and clean user interface

## Installation

1. Clone the repository:

```bash
https://github.com/Navenesvar/Admin_panel_Registration_Django.git
cd Admin_panel_Registration_Django
```
## Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:
On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
Run migrations:

```bash
python manage.py migrate
```
Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```
Start the development server:

```bash
python manage.py runserver
```
Visit http://127.0.01:8000 in your browser

Visit http://127.0.0.1:8000/admin/ in your browser and log in with the superuser credentials.

Visit http://127.0.0.1:8000/register/ to access the registration page.
