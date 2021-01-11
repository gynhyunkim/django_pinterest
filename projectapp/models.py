from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateTimeField(auto_now=True)