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
    GREY = '4d4e4e'
    DARKBLUE = '001f54'
    BLUE = '1f487e'
    LIGHTBLUE = '59a5d8'
    LIGHTBROWN = '926639'
    BROWN = '6f5232'
    TURQUOISE = '048ba8'
    DARKGREEN = '137547'
    GREEN = '528029'
    LIGHTGREEN = '8ea604'
    YELLOW = 'eabc20'
    ORANGE = 'f56416'
    RED = 'e71d36'
    DARKRED = '671934'
    PINK = 'd90368'
    PURPLE = 'a4036f'
    COLOR_OPTIONS = [
        (GREY, 'grey'),
        (DARKBLUE, 'dark blue'),
        (BLUE, 'blue'),
        (LIGHTBLUE, 'light blue'),
        (LIGHTBROWN, 'light brown'),
        (BROWN, 'brown'),
        (TURQUOISE, 'turquoise'),
        (DARKGREEN, 'dark green'),
        (GREEN, 'green'),
        (LIGHTGREEN, 'light green'),
        (YELLOW, 'yellow'),
        (ORANGE, 'orange'),
        (RED, 'red'),
        (DARKRED, 'dark red'),
        (PINK, 'pink'),
        (PURPLE, 'purple'),
    ]
    # yellow, orange, red, pink, rose, purple, turquoise, blue, darkblue, darkred

    color = models.CharField(verbose_name='Color',
        max_length=6,
        choices=COLOR_OPTIONS,
        default=GREY)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(TimeStamped):
    name = models.CharField(verbose_name='Task Name', max_length=80)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    importance = models.IntegerField(verbose_name='Importance', default=50)
    due_date = models.DateTimeField(verbose_name='Due Date', default=timezone.now)
