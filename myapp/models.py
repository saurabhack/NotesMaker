from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AddNotes(models.Model):
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    notes = RichTextField(blank=True,null=True)