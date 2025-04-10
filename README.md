# LogIQids Referral System

This is a backend project built using **Django** and **SQLite3** for handling user registration and referral tracking, as part of a backend engineering assignment.

## Features

- User Registration with optional referral code
- Login functionality
- Unique referral code generated for each user
- Tracking of referred users
- Admin access via Django Admin panel

## Tech Stack

- Python 3.10+
- Django 4.x
- SQLite3 (default DB, can be replaced with PostgreSQL/MySQL)
- Django Rest Framework

## Setup Instructions

 **Clone the repository**  
   bash
   git clone https://github.com/yourusername/logiqids_referral_system.git
   cd logiqids_referral_system
   
  Create a virtual environment & activate it:
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py makemigrations
python manage.py migrate

Create superuser (optional, for admin access):
python manage.py createsuperuser

Run the server:
python manage.py runserver

API Endpoints
Method	Endpoint	Description
POST	/register/	Register a new user
POST	/login/	Login with email & password
GET	/referrals/	Get referred users (if logged in)

Folder Structure: 
accounts/ - Contains models, views, serializers for user and referral logic

logiqids_referral/ - Django project settings

db.sqlite3 - Default database

requirements.txt - Python dependencies

Future Improvements: 
Add email verification

Add support for social logins

Rate limiting for abuse prevention

Referral dashboard analytics


