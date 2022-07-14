from django.db import models


class TemperatureReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        db_table = "temperature_reading"
        indexes = [
            models.Index(fields=["timestamp"], name="timestamp_idx"),
        ]
        get_latest_by = ["-timestamp", "id"]

    def __str__(self):
        return f"TemperatureReading {self.timestamp}:{self.value}"
