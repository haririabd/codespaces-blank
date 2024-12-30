from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.name