from django.db import models


class Book(models.Model):
    title = models.CharField( max_length=250,blank=False,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=3,blank=False,null=False)
    author = models.CharField("author name", max_length=100,blank=False,null=False)
    publicationdate = models.DateField()
    # updated_at = models.DateField(auto_now = True , null= False)
    
    def __str__(self):
        return self.title