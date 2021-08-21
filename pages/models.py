from django.db import models

# Create your models here.
class Teams(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image =models.ImageField(upload_to='teams/')
    address = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    twitter_link = models.URLField()
    facebook_link = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
