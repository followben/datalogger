import graphene
from django.db.models import Max, Min
from graphene_django import DjangoObjectType

from challenge.datalogger.models import TemperatureReading


class DateTime(graphene.DateTime):
    @staticmethod
    def serialize(dt):
        return dt.isoformat(timespec="seconds")


class TemperatureReadingType(DjangoObjectType):
    class Meta:
        model = TemperatureReading
        fields = ("id", "timestamp", "value")

    timestamp = graphene.Field(DateTime)


class TemperatureStatisticsType(graphene.ObjectType):
    min = graphene.Float()
    max = graphene.Float()


class Query(graphene.ObjectType):
    current_temperature = graphene.Field(TemperatureReadingType)
    temperature_statistics = graphene.Field(
        TemperatureStatisticsType,
        after=DateTime(),
        before=DateTime(),
    )

    def resolve_current_temperature(root, _):
        return TemperatureReading.objects.latest()

    def resolve_temperature_statistics(root, _, after: DateTime, before: DateTime):
        if not after and not before:
            raise ValueError("Either before and or after are required")
        queryset = TemperatureReading.objects.filter(timestamp__gte=after, timestamp__lte=before).aggregate(
            Min("value"), Max("value")
        )
        return TemperatureStatisticsType(
            min=queryset["value__min"],
            max=queryset["value__max"],
        )
