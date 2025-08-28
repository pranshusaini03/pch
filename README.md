# PetCareHub (Django)

A Django 5 project for a pet-care hub featuring product listings, grooming and health services, adoption directories, carts, and authentication.

## Features
- Adoption listings by city (`adoption`)
- Grooming providers (`grooming`)
- Health services (`health`)
- Product catalog (`product`)
- Shopping cart (`cart`)
- Authentication (`login`)
- Service forms (`form`)

## Requirements
- Python 3.10+
- pip

## Quickstart

```bash
# 1) Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
. .venv/Scripts/Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Apply migrations
cd pch-main
python manage.py migrate

# 4) (Optional) Create an admin user
python manage.py createsuperuser

# 5) Run the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Project layout

- Django project root: `pch-main/`
- Settings module: `pch-main/petcarehub/settings.py`
- Apps: `adoption`, `cart`, `form`, `grooming`, `health`, `login`, `product`
- Templates: `pch-main/templates/`
- Static: `pch-main/static/` (served in development via `STATICFILES_DIRS`)
- Media uploads: `pch-main/media/`

## Static & Media
- `STATIC_URL` is `/static/`; dev files are under `static/`.
- `MEDIA_URL` is `/media/`; uploaded files stored under `media/`.
- ImageField usage requires Pillow (included in requirements).

## Common commands
```bash
# Make migrations for model changes
python manage.py makemigrations
python manage.py migrate

# Collect static files for production (if needed)
python manage.py collectstatic --noinput
```

## Notes
- The project uses SQLite by default (`db.sqlite3`). No extra DB setup is required for development.
- Update `ALLOWED_HOSTS` and set `DEBUG = False` before deploying.
- If running on Windows and encountering timezone issues, install `tzdata`. 
