web: gunicorn seostat.wsgi
celery: celery -A seostat beat -l DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler 