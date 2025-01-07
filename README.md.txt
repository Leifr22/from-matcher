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
