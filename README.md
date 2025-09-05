# Volvet - Modern Django eCommerce Platform

## Features
  - User authentication
  - Admin dashboard for managing users and content
  - Responsive design
  - Search functionality
  - Pagination
  - Logo change using admin panel
    
A feature-rich eCommerce platform built with Django, offering a seamless shopping experience with robust admin controls and user management.

## ✨ Key Features

- 👤 User Authentication & Authorization
- 🛍️ Product Management
- 🛒 Shopping Cart Functionality
- 📦 Order Processing
- 🔍 Advanced Search & Filtering
- 📱 Responsive Design
- ⚡ RESTful API Endpoints
- 🎨 Customizable Theme
- 📊 Admin Dashboard
- 🖼️ Dynamic Logo Management
- 📄 Content Management System (CMS)
- 📝 Order Tracking

## 🛠️ Tech Stack

- **Backend:** Django 5.0
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript
- **CSS Framework:** Bootstrap 4
- **Icons:** Font Awesome
- **Other Libraries:**
  - django-crispy-forms
  - Pillow (for image processing)
  - psycopg2-binary
  - django-environ

## 📁 Project Structure
```
volvet/
├── manage.py
├── requirements.txt
├── volvet/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── accounts/
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── cms/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
│   ├── products/
│   ├── banners/
│   └── logos/
├── templates/
│   └── base.html
└── docs/
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/volvet.git
cd volvet
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Start development server:
```bash
python manage.py runserver
```

8. Visit https://mahede182.pythonanywhere.com/ in your browser

## 💻 Admin Interface

Access the admin interface at https://mahede182.pythonanywhere.com/admin admin to:

_Credential_

admin

1234

- Manage products and categories
- Handle user accounts
- Process orders
- Update site settings
- Manage content

## 🔧 Configuration

Key settings can be configured through environment variables:
- `DEBUG`: Set to False in production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: Database connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Your Name - [@yourusername](https://twitter.com/yourusername)
Project Link: [https://github.com/yourusername/volvet](https://github.com/yourusername/volvet)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- All contributors
