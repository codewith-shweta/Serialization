from django.db import models
from django.utils import timezone

# Create your models here.
class Snippets(models.Model):
    created_at= models.DateTimeField(default=timezone.now)
    title= models.CharField(max_length=20)
    code= models.TextField()
    lineous= models.BooleanField(default=False)
    language= models.CharField()
    style= models.CharField()
