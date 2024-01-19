from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    date_joined = models.DateField(null=True) 
    time = models.TimeField(null=True)
    email = models.EmailField(null=True)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email}"