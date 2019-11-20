from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    message= models.CharField(max_length=255)
    file_data=models.FileField(upload_to='media',null=True,blank=True)

    def __str__(self):
        return self.name +' '+ self.message 
