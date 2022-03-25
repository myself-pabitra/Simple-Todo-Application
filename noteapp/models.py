from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(max_length=250,blank=False,null=False)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.title)