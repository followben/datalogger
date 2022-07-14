from django.contrib import admin

from challenge.datalogger.models import TemperatureReading


@admin.register(TemperatureReading)
class ChallengeAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
