from django.db import models

class Form(models.Model):
    name=models.CharField(max_length=255)
    fields=models.JSONField()

    def __str__(self):
        return self.name
# Create your models here.
