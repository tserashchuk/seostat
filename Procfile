web: gunicorn seostat.wsgi
celery: celery -A seostat worker -l info -c 4 enable_events