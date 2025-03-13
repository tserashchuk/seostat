web: gunicorn seostat.wsgi
celery: celery -A seostat beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler