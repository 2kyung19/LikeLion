from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def summary(self):
        return self.body[:20]