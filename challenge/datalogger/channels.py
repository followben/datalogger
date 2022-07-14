from django.conf import settings

from challenge.datalogger.consumers import FeedConsumer

channel = {settings.CHANNEL_NAME: FeedConsumer.as_asgi()}
