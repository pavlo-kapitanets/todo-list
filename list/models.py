from django.db import models
from django.forms import SelectDateWidget


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)
    completion = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="tags")

    class Meta:
        ordering = ["completion", "creation_date"]

    def __str__(self):
        return (f"{self.description}: "
                f"Created: {self.creation_date.strftime('%B %d, %Y %H:%M %p')}")

