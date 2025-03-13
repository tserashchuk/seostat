web: gunicorn seostat.wsgi
celery: celery -A seostat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler 