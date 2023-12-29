from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
from django.urls import reverse
# Create your models here.

class MoodData(models.Model):
    MOODCHOICES = (
        ("Excited", "Excited"),
        ("Happy", "Happy"),
        ("Relaxed", "Relaxed"),
        ("Sad", "Sad"),
        ("Angry", "Angry"),
    )
    dateposted = models.DateField(default=timezone.now)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moodtype = models.CharField(choices=MOODCHOICES, max_length=20)
    token = models.CharField(max_length=17, primary_key=True, unique=True)

    def save(self, *args, **kwargs):
       
        if not self.token:
            self.token = secrets.token_hex(16)  

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.moodtype} at {self.dateposted}'
    