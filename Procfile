release: python manage.py migrate --no-input && python manage.py shell < create_admin.py
web: gunicorn amazon_clone.wsgi:application