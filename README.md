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




![Screenshot 2025-04-10 163030](https://github.com/user-attachments/assets/348658f1-0805-4e98-8cd7-83c42aaec3f8)
![Screenshot 2025-04-10 112250](https://github.com/user-attachments/assets/222083ba-e782-4f00-bfbc-26f766569428)
![Screenshot 2025-04-10 112238](https://github.com/user-attachments/assets/b06b95e7-e09a-49d8-8be6-21d7b6737e17)
![Screenshot 2025-04-10 112224](https://github.com/user-attachments/assets/6602706e-11c5-4801-934b-c173f227a602)
![Screenshot 2025-04-10 112211](https://github.com/user-attachments/assets/406346c1-7480-49bc-83d3-846e6e88212c)
