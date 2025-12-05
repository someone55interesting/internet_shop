# amazon_clone/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon_clone.settings')

application = get_wsgi_application()

# ⚠️ ИСПРАВЛЕННЫЙ ПУТЬ: нужно подняться на один уровень выше
# os.path.dirname(__file__) — это amazon_clone/
# os.path.dirname(os.path.dirname(__file__)) — это /opt/render/project/src/ (корневая папка)
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles'))
