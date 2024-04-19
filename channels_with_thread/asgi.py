import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from data_app.consumers import  TestConsumer, NewConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_with_thread.settings')

# application = get_asgi_application()
django_application = get_asgi_application()

ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi()),
    path('ws/data_genrate/', NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': django_application,
    'websocket': URLRouter(ws_patterns)
})

