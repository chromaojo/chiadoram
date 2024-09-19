from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

# Create your models here.

class Post(models.Model):
    FullName = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phoneNumber = models.IntegerField()
    subject = models.CharField(max_length=100)
    message_body = models.TextField(blank=True)
    sent_at = models.DateTimeField(default=datetime.now)
    message_id = models.UUIDField(default=uuid.uuid4)