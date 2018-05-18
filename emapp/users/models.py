from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # some other attributes the emauser model is for
