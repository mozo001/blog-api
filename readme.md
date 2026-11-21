# Bloger

A Django and Django REST Framework (DRF) application providing both server-rendered HTML views and a RESTful JSON API for managing blog posts with UUIDv4 primary keys and OpenAPI 3.0 documentation via `drf-spectacular`.

## Features

- **Dual Interface:** Server-rendered HTML views (`index.html`, `blog_detail.html`, `create_blog.html`, `update_blog.html`) alongside JSON REST API endpoints.
- **Full CRUD Support:** Create, retrieve, full/partial update (`PUT`/`PATCH`), and delete blog posts.
- **UUIDv4 Identifiers:** Non-sequential `UUIDField` primary keys (`uuid4`) for blog records.
- **Environment-Based Configuration:** Managed via `django-environ` and `.env` files for clean separation of secrets and environment settings.
- **Interactive API Docs:** OpenAPI 3.0 schema with Swagger UI and ReDoc via `drf-spectacular`.
- **Modular Layout:** Separation between Django project configuration (`src/`) and the feature app (`blog/`).

## Tech Stack

- **Language & Framework:** Python 3, Django, Django REST Framework (DRF)
- **Environment Management:** `django-environ`
- **API Documentation:** `drf-spectacular` (OpenAPI 3.0)
- **Database:** SQLite (default in development; PostgreSQL recommended for production)

## Project Structure

```text
.
├── blog/
│   ├── migrations/       # Database migrations
│   ├── templates/        # Blog HTML templates (index, detail, create, update)
│   ├── admin.py          # Django admin registration
│   ├── apps.py           # App configuration
│   ├── models.py         # Blog model definition
│   ├── serializers.py    # DRF serializers
│   ├── tests.py          # Unit and integration tests
│   ├── urls.py           # API and HTML route definitions
│   └── views.py          # DRF API views and HTML template views
├── src/
│   ├── templates/        # Project-level templates
│   ├── asgi.py           # ASGI entry point
│   ├── settings.py       # Django settings (configured with django-environ)
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI entry point
├── .env.example          # Example environment variables template
├── manage.py             # Django CLI entry point
├── requirements.txt      # Python dependencies
└── README.md
```

## Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/mozo001/blog-api.git
cd blog-api
```

### 2. Create and Activate a Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*(Ensure `django-environ` is included in `requirements.txt`.)*

### 4. Configure Environment Variables

Copy the example environment file to `.env` and update the values for your local environment:

**Linux / macOS:**
```bash
cp .env.example .env
```

**Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
```

Example `.env` configuration:

```env
DEBUG=True
SECRET_KEY=replace-with-a-strong-unique-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

> **Security Note:** Never commit your real `.env` file or production `SECRET_KEY` to version control. Ensure `.env` is listed in `.gitignore`, and keep `.env.example` populated with placeholder values only.

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## API Documentation

When `drf-spectacular` routes are configured in your URLs, documentation is exposed at:

- **Swagger UI:** `/api/docs/` or `/blogs/docs/` (verify exact path in `src/urls.py` / `blog/urls.py`)
- **ReDoc:** `/api/redoc/` or `/blogs/redoc/`
- **OpenAPI Schema:** `/api/schema/` or `/blogs/schema/`

## Endpoints

> **Note:** Check `src/urls.py` to confirm whether `blog.urls` is mounted at root (`/`) or under a prefix such as `/blog/`.

### REST API Endpoints (`blog/urls.py`)

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `blogs/` | List all blog posts |
| `POST` | `blogs/create/` | Create a new blog post |
| `GET` | `blogs/<uuid:pk>/` | Retrieve a single blog post |
| `PUT` | `blogs/<uuid:pk>/update/` | Full update of a blog post |
| `PATCH` | `blogs/<uuid:pk>/update/` | Partial update of a blog post |
| `DELETE` | `blogs/<uuid:pk>/delete/` | Delete a blog post |

### HTML Views (`blog/urls.py`)

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Blog list page (`index.html`) |
| `GET` / `POST` | `create/` | Create blog form |
| `GET` | `<uuid:pk>/` | Blog detail page (`blog_detail.html`) |
| `GET` / `POST` | `<uuid:pk>/update/` | Update blog form (`update_blog.html`) |
| `GET` / `POST` | `<uuid:pk>/delete/` | Delete confirmation / action |

## Data Model

### `Blog` (`blog.models.Blog`)

Ordered by `-created_at` (newest first).

| Field | Type | Constraints / Notes |
| :--- | :--- | :--- |
| `id` | `UUIDField` | Primary key, auto-generated `uuid4`, `editable=False` |
| `title` | `CharField` | `max_length=255` |
| `description` | `CharField` | `max_length=500` |
| `content` | `TextField` | Main post body |
| `created_at` | `DateTimeField` | Auto-set on creation (`auto_now_add=True`) |
| `updated_at` | `DateTimeField` | Auto-updated on save (`auto_now=True`) |

## Production Readiness & Best Practices

To move from local development to a production-grade deployment:

1. **Secrets & Environment Config:** In `src/settings.py`, read `.env` (rather than `.env.example`) via `environ.Env.read_env(BASE_DIR / ".env")`, generate a new cryptographically secure `SECRET_KEY` for production, set `DEBUG=False`, and configure `ALLOWED_HOSTS` via environment variables.
2. **Production Database:** Replace SQLite (`db.sqlite3`) with PostgreSQL (`DATABASE_URL` via `env.db()`) and manage schema changes strictly through versioned migrations (`python manage.py migrate`).
3. **WSGI/ASGI & Reverse Proxy:** Serve the app with Gunicorn (or Uvicorn for async) behind Nginx, with HTTPS/TLS enabled.
4. **Static Files:** Configure `STATIC_ROOT`, run `python manage.py collectstatic`, and serve static assets via WhiteNoise or a reverse proxy/CDN.
5. **Security, Auth & Pagination:** Add authentication/permissions (`IsAuthenticated` or role/ownership checks as needed), configure CORS/CSRF settings explicitly, enable DRF pagination/throttling, and ensure user inputs are validated/sanitized before rendering HTML or saving records.
6. **Testing & CI:** Expand unit and API tests in `blog/tests.py` and run `python manage.py test` (plus linting/type checks) in CI before merging or deploying.