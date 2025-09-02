# Django Blog Generator

A simple Django REST API that generates blogs from any given topic using OpenAI.  
This project is open-source and designed to be minimal, so you can extend it for your own needs.

---

## Features
- Accepts a topic as input
- Generates a well-structured blog with a title, content, and subheadings
- Returns blog content as JSON
- Easy to integrate into any frontend or CMS

---

## Requirements
- Python 3.9+
- Django 4+
- OpenAI API Key

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-blog-generator.git
   cd django-blog-generator

   Create and activate a virtual environment

python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows


Install dependencies

pip install django djangorestframework python-dotenv openai


Set up environment variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


Run migrations

python manage.py migrate


Start the server

python manage.py runserver

Usage
Endpoint

POST /api/generate-blog/

Request Body
{
  "topic": "The Impact of AI on Remote Work"
}

Response
{
  "title": "The Impact of AI on Remote Work",
  "topic": "The Impact of AI on Remote Work",
  "content": "Engaging introduction...\n\n## Subheading 1\nContent...\n\n## Subheading 2\nContent...\n\n## Conclusion\nTakeaway..."
}

Project Structure
myproject/
│── myproject/           # Django project settings
│── blog/                # Blog app with API
│   ├── views.py         # Blog generator logic
│   ├── urls.py          # API routes
│── manage.py
│── .env                 # Environment variables
│── requirements.txt     # Dependencies
│── README.md

Extending

Save generated blogs to a database

Export blogs as Markdown files

Add scheduling with Celery

Build a frontend for easier usage

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.


Do you want me to also create a **`requirements.txt`** file so people can install dependencies with just `pip in
