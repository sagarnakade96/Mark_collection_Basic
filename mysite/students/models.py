
from django.db import models

# Create your models here.
class Students(models.Model):
    usn=models.CharField(max_length=100, primary_key=True)
    fname= models.CharField(max_length=100, default="")
    lname=models.CharField(max_length=100,default="")
    ten_ma=models.CharField(max_length=100,default="")
    tw_ma=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.usn
    