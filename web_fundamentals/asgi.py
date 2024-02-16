"""
ASGI config for web_fundamentals project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack 
# Channels supports Django standard Auth which checks client's session.
# AuthMiddleware requires SessionMiddleware to function, which itself
# requires CookieMiddleware. For convenience, these are also provided
# as a combined callable called AuthMiddlewareStack that includes all three.
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_fundamentals.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
      URLRouter(
        chat.routing.websocket_urlpatterns
      )
    )
})
