# Admin Panel Registration Project

This project is a simple Django web application for user registration with an admin panel.

## Features

- User registration with username, email, and password
- Admin panel for managing user registrations
- Bootstrap for a responsive and clean user interface

## Installation

1. Clone the repository:

```bash
https://github.com/Navenesvar/Admin_panel_Registration_Django.git
cd Admin_panel_Registration_Django
```
## Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:
On Windows:

```
venv\Scripts\activate
```
On macOS/Linux:

```
source venv/bin/activate
```
Run migrations:

```
python manage.py migrate
```
Create a superuser (admin) account:

```
python manage.py createsuperuser
```
Start the development server:

```
python manage.py runserver
```
Visit http://127.0.01:8000 in your browser

Visit http://127.0.0.1:8000/admin/ in your browser and log in with the superuser credentials.

Visit http://127.0.0.1:8000/register/ to access the registration page.
