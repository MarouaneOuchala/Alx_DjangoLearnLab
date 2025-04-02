# Django Blog

A simple blog application built with Django 5.2. This project demonstrates basic Django features including models, templates, static files, and user authentication.

## Features

- User authentication (login, logout)
- Blog post creation and management
- Responsive design
- Modern UI with CSS animations
- Interactive features with JavaScript

## Project Structure

```
django_blog/
├── blog/                  # Blog application
│   ├── migrations/        # Database migrations
│   ├── static/           # Static files (CSS, JS)
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   └── views.py          # View functions
└── django_blog/          # Project configuration
    ├── settings.py       # Project settings
    └── urls.py          # URL configuration
```

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd django_blog
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the blog.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 