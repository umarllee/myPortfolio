from django.db import models

class Contact(models.Model):
        name= models.CharField(max_length=50)
        lastname= models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        message= models.TextField(blank= True)

        def __str__(self):
            return self.email 

  