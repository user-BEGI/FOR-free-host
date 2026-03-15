"""
WSGI config for burger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'burger.settings')

application = get_wsgi_application()

from django.contrib.auth import get_user_model
User = get_user_model()
try:
    if not User.objects.filter(username='begi').exists():
        User.objects.create_superuser('begi', 'begibrol7@gmail.com', 'admin123')
        print("Superuser created: admin / admin123")
except:
    pass