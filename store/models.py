from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic_url = models.CharField(max_length= 1000, null=True, blank=True)
    location = models.CharField(max_length= 100, null=True, blank=True)
    phone = models.CharField(max_length= 100, null=True, blank=True)
        
    def __str__(self) -> str:
        return self.username



class Category(models.Model):
    title = models.CharField(max_length= 100)

class Item(models.Model):
    
    NEW_ITEM = 'NEW'
    USED_ITEM = 'USED'
    REFURBISED_ITEM = 'REFURBISHED'
   
    ITEM_CONDITION = [
       (NEW_ITEM, 'NEW'),
       (USED_ITEM, 'USED'),
       (REFURBISED_ITEM, 'REFURBISHED')
       
   ]
    
    
    name = models.CharField(max_length= 50)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')
    descripton = models.TextField(null=True)
    image_url = models.CharField(max_length= 1000, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    condition = models.CharField(max_length= 25, choices=ITEM_CONDITION,default=NEW_ITEM)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name