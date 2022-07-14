import pytest
from django.conf import settings
from graphene_django.utils.testing import graphql_query

from challenge.datalogger.models import TemperatureReading

# @pytest.fixture
# def client_query(client):
#     def wrapper(*args, **kwargs):
#         return graphql_query(*args, **kwargs, client=client)

#     return wrapper


@pytest.fixture(scope="session")
def django_db_modify_db_settings():
    settings.DATABASES = {"default": {"USERNAME": "btovold", "PASSWORD": ""}}


@pytest.mark.django_db
def test_user_create(django_db_modify_db_settings):
    TemperatureReading.objects.create(value=70)


# def test_some_query(client_query):
#     response = client_query(
#         """
#         query {
#             currrentTemperature {
#                 timestamp
#                 value
#             }
#         }
#         """
#     )

#     content = json.loads(response.content)
#     assert "errors" not in content
