# models.py
from django.db import models

class Task(models.Model):  # Change the model name to Task
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)  # Rename is_completed to status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
