from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=120)
    due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
    