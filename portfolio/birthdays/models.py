from django.db import models


class Birthday(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} ({self.date})"

