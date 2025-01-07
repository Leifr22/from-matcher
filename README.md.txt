Form Matcher
Form Matcher is a Django-based web application that identifies the most suitable form template for a given set of fields. If no matching template is found, it dynamically determines the field types based on validation rules and returns their types.

Features
Template Matching: Stores form templates with unique field names and types.
Field Types:
email: Validates standard email format.
phone: Validates phone numbers in the format +7 xxx xxx xx xx.
date: Supports formats DD.MM.YYYY or YYYY-MM-DD.
text: General text fields (no validation required).
Dynamic Typing: If no form matches, identifies field types on the fly.
Built With:
Django for backend development.
PostgreSQL for data storage.
Installation and Setup
Follow the steps below to set up the project:

Prerequisites
Python 3.6+
PostgreSQL
Steps
Clone the Repository:

bash

git clone https://github.com/your-username/form-matcher.git
cd form-matcher
Set Up a Virtual Environment:

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash

pip install -r requirements.txt
Configure Database: Open form_matcher/settings.py and update the DATABASES section with your PostgreSQL credentials:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply Migrations:

bash

python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash

python manage.py runserver
Usage
Add Form Templates: Use the Django admin interface or populate the database programmatically with form templates. Each template consists of a name and a set of fields with defined types.

Send a POST Request: Endpoint: /get_form/
Content-Type: application/json

Example Request:

json

{
    "f_name1": "value1",
    "f_name2": "value2"
}
Example Responses:

If a matching form template is found:
json

{
    "template_name": "Contact Form"
}
If no matching template is found:
json

{
    "f_name1": "email",
    "f_name2": "phone"
}
Running Tests
Prepare the Test Environment: Ensure your database is configured correctly for testing.

Run Tests:

bash

python manage.py test
Example Request Using curl
bash

curl -X POST http://127.0.0.1:8000/get_form/ \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "phone": "+7 123 456 78 90"}'