from django.db import models

# Create your models here.

class DataN(models.Model):
    #user =
    note_name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    note_data =models.TextField()
    

