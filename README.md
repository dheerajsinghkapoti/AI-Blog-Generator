# Django Blog Generator

A minimal Django REST API that generates blogs from any given topic using OpenAI. It is open-source and intentionally small so it can be extended for custom needs.

## Features
- Accepts a topic as input and generates a well-structured blog with title, subheadings, and content.  
- Returns blog content as JSON for easy integration with any frontend or CMS.  
- Minimal surface area to extend (persistence, exports, scheduling, UI).  

## Requirements
- Python 3.9+ and Django 4+  
- OpenAI API key (via environment variables)  
- Django REST Framework  

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/django-blog-generator.git
cd django-blog-generator
````

Create and activate a virtual environment:

```bash
# Linux/Mac
python -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate
```

Install dependencies:

**Option A: pip**

```bash
pip install django djangorestframework python-dotenv openai
```

**Option B: requirements.txt (recommended)**

```bash
pip install -r requirements.txt
```

Set environment variables. Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

Apply migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

## Usage

**Endpoint**

```
POST /api/generate-blog/
```

**Request body**

```json
{
  "topic": "The Impact of AI on Remote Work"
}
```

**Response**

```json
{
  "title": "The Impact of AI on Remote Work",
  "topic": "The Impact of AI on Remote Work",
  "content": "Engaging introduction...\n\n## Subheading 1\nContent...\n\n## Subheading 2\nContent...\n\n## Conclusion\nTakeaway..."
}
```

## Project structure

```text
myproject/
│── myproject/            # Django project settings
│── blog/                 # Blog app with API
│   ├── views.py          # Blog generator logic
│   ├── urls.py           # API routes
│── manage.py
│── .env                  # Environment variables
│── requirements.txt      # Dependencies
│── README.md
```

## Extending

* Save generated blogs to a database
* Export blogs as Markdown files
* Add scheduling with Celery
* Build a frontend for easier usage

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

## Example requirements.txt

```text
Django>=4.0,<5.0
djangorestframework>=3.14
python-dotenv>=1.0
openai>=1.0
```

```

