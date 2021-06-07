from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name