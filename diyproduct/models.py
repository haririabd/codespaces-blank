from django.db import models

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories(): 
        return Category.objects.all() 
  
    def __str__(self): 
        return self.name

class User(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
  
    # to save the data 
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True

        return False

class Store(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def register(self):
        self.save()
    
    @staticmethod
    def get_all_store(): 
        return Store.objects.all() 
  
    def __str__(self): 
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50)
    name = models.ForeignKey("Store", on_delete=models.CASCADE)
    po_date = models.DateField()