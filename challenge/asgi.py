"""
ASGI config for challenge project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from challenge.datalogger.channels import channel

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "challenge.settings")

asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": asgi_app,
        "channel": ChannelNameRouter(channel),
    }
)
