from django.db import models

# Create your models here.

class Message(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)