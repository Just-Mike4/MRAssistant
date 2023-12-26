from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class MoodData(models.Model):
    MOODCHOICES=(
        ('Excited','Excited'),
        ('Happy','Happy'),
        ('Relaxed','Relaxed'),
        ('Sad','Sad'),
        ('Angry','Angry'),
    )
    dateposted=models.DateField(default=timezone.now)
    description=models.TextField()
    user=models.ForeignKey(User)
    moodmatrix=models.CharField(choices=MOODCHOICES)