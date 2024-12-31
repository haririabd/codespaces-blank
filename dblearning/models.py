from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Profile referred to geeks for geek: https://www.geeksforgeeks.org/how-to-extend-user-model-in-django/
# Also here : https://medium.com/@karimdhrif4444/mastering-user-management-comprehensive-guide-to-extending-djangos-user-model-51c2ccd793d4

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    # It’s suggested, but not required, that the name of a ForeignKey field (state in the example below) be the name of the model (State in below example), lowercase.
    # You can call the field whatever you want
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name