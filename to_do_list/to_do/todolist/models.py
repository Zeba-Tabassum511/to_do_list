from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=500)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    