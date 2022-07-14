import os

from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "app.config.settings"


def pytest_configure():
    settings.DATABASES = {"default": {"USERNAME": "btovold", "PASSWORD": ""}}
