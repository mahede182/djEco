# Volvet - a django ecommerce

## Features
  - User authentication
  - Admin dashboard for managing users and content
  - Responsive design
  - Search functionality
  - Pagination
  - Logo change using admin panel

## Packages Used
- Django
- psycopg2 (for PostgreSQL)
- Any other relevant packages

## Folder Structure
```
.
├── README.md
├── requirements.txt
├── volvet
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── media
│   └── banners
├── static
│   └── css
├── templates
│   └── base.html
├── .gitignore
├── .gitattributes
└── .gitlab-ci.yml

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mahede182/djEco.git
   cd yourproject ```
2. Install the required packages:   
   ```bash
   pip install -r requirements.txt ```
3. Run the development server:
   ```bash
   python manage.py runserver ```
4. Open your browser and navigate to http://localhost:8000/

