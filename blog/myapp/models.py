from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Guest(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:20]

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title