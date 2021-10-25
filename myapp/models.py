from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.first_name

class BlogDe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name