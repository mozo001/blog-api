# Bloger API

A RESTful API built with Django and Django REST Framework for managing blog posts. The application supports full CRUD operations with UUID-based primary keys and includes automated OpenAPI 3.0 documentation via `drf-spectacular`.

## Features

* **CRUD Operations**: Create, retrieve, update, and delete blog posts.
* **UUID Identifiers**: Secure, non-sequential `UUIDv4` primary keys for blog resources.
* **Interactive API Documentation**: Integrated Swagger UI, ReDoc, and downloadable OpenAPI schema.
* **Modular Architecture**: Clean separation between core project configuration (`src`) and application logic (`blog`).

## Technology Stack

* **Backend Framework**: Django
* **API Toolkit**: Django REST Framework (DRF)
* **API Documentation**: `drf-spectacular` (OpenAPI 3.0)
* **Database**: SQLite (default for development; configurable for PostgreSQL/MySQL in production)

## Project Structure

```text
Bloger/
├── blog/                   # Main application directory
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Django admin configurations
│   ├── apps.py             # App configuration
│   ├── models.py           # Blog database model
│   ├── serializers.py      # DRF serializers
│   ├── tests.py            # Unit and integration tests
│   ├── urls.py             # Application-level routing
│   ├── views.py            # API views and business logic
│   └── requirments.txt     # Project dependencies
├── src/                    # Project configuration directory
│   ├── asgi.py             # ASGI entry point
│   ├── settings.py         # Global Django & DRF settings
│   ├── urls.py             # Root URL routing and documentation endpoints
│   └── wsgi.py             # WSGI entry point
└── manage.py               # Django command-line utility
```

## Prerequisites

* Python 3.10 or higher
* `pip` (Python package installer)
* `virtualenv` or `venv`

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd Bloger
   ```

2. **Create and Activate a Virtual Environment**

   On Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**

   Note: Ensure the requirements file path matches your directory layout (`blog/requirments.txt`).

   ```bash
   pip install -r blog/requirments.txt
   ```

   *(Note: If you encounter package naming issues with `django_rest_framework` in the requirements file, install `djangorestframework` directly via `pip install django djangorestframework drf-spectacular`.)*

4. **Apply Database Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**

   To access the Django Admin interface:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`.

## API Documentation

This project uses `drf-spectacular` to generate OpenAPI 3.0 compliant documentation. Once the server is running, you can inspect and test the endpoints using the following URLs:

* **Swagger UI (Interactive Docs)**: [http://127.0.0.1:8000/blogs/docs/](http://127.0.0.1:8000/blogs/docs/)
* **ReDoc (Reference Docs)**: [http://127.0.0.1:8000/blogs/redoc/](http://127.0.0.1:8000/blogs/redoc/)
* **OpenAPI Schema (YAML/JSON)**: [http://127.0.0.1:8000/blogs/schema/](http://127.0.0.1:8000/blogs/schema/)

## API Endpoints

| HTTP Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Retrieve a list of all blog posts |
| `POST` | `/blogs/create/` | Create a new blog post |
| `GET` | `/blogs/<uuid:pk>/` | Retrieve details of a specific blog post |
| `PUT` / `PATCH` | `/blogs/<uuid:pk>/update/` | Update an existing blog post |
| `DELETE` | `/blogs/<uuid:pk>/delete/` | Delete a specific blog post |
| `GET` | `/admin/` | Access the Django administration panel |

## Data Model

### Blog (`blog.models.Blog`)

| Field | Type | Constraints / Details |
| :--- | :--- | :--- |
| `id` | `UUIDField` | Primary key, auto-generated (`uuid4`), non-editable |
| `title` | `CharField` | Maximum length of 150 characters |
| `description` | `TextField` | Main content body of the blog post |
| `created_at` | `DateTimeField` | Automatically set when the record is created |
| `updated_at` | `DateTimeField` | Automatically updated whenever the record is saved |

## Production Considerations

Before deploying this application to a production environment, ensure the following steps are completed:

1. **Environment Variables**: Move `SECRET_KEY`, `DEBUG` (set to `False`), and database credentials out of `src/settings.py` into environment variables.
2. **Allowed Hosts**: Configure `ALLOWED_HOSTS` in `src/settings.py` with your production domain names or IP addresses.
3. **Database**: Switch from SQLite to a production-grade relational database such as PostgreSQL.
4. **Application Server**: Serve the application using a production WSGI/ASGI server such as Gunicorn or Uvicorn behind a reverse proxy like Nginx.
5. **Static Files**: Run `python manage.py collectstatic` and configure static file serving (e.g., via WhiteNoise or a CDN).
