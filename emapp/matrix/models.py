from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TimeStamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Topic(TimeStamped):
    name = models.CharField(verbose_name='Topic Name', max_length=50)
    color = models.CharField(verbose_name='Color', max_length=6)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(TimeStamped):
    name = models.CharField(verbose_name='Task Name', max_length=80)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    importance = models.IntegerField(verbose_name='Importance', default=50)
    due_date = models.DateTimeField(verbose_name='Due Date', default=timezone.now)
