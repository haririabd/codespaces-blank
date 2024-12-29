from django.db import models

# Create your models here.

class ProductCategory(models.Model): 
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories(): 
        return ProductCategory.objects.all() 
  
    def __str__(self): 
        return self.name

class State(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self): 
        return self.state

class Brand(models.Model):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand    

class User(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    store = models.ForeignKey("Store", on_delete=models.DO_NOTHING)
  
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
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, null=True)
    store_name = models.CharField(max_length=100)
    store_code = models.CharField(max_length=50)
    state = models.ForeignKey("State", on_delete=models.CASCADE)

    def register(self):
        self.save()
    
    @staticmethod
    def get_all_store(): 
        return Store.objects.all() 
  
    def __str__(self):
        return self.store_name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50)
    store_name = models.ForeignKey("Store", on_delete=models.CASCADE)
    po_date = models.DateField()