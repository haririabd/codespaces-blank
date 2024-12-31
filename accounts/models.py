from django.db import models
from django.contrib.auth.models import User
from dblearning.models import Store

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username