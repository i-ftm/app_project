from django.db import models
class user(models.Model):
    name = models.CharField("user name", max_length=100,blank=False,null=False)
    email = models.EmailField("email address", blank=False)
    password = models.CharField(max_length=100,blank=False,null=False)
    
class book(models.Model):
    titel = models.CharField( max_length=250,blank=False,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=3,blank=False,null=False)
    author = models.CharField("author name", max_length=100,blank=False,null=False)
    publicationdate = models.DateField(auto_now_add= True , null= False)
    updated_at = models.DateField(auto_now = True , null= False)