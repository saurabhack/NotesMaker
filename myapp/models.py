from django.db import models

# Create your models here.
class AddNotes(models.Model):
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    notes = models.TextField()
