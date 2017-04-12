from django.db import models

# Create your models here.
class Image(object):
    """Image is an object that holds the url and description of an image."""
    image = models.ImageField(upload_to="uploads/images")
    description = models.TextField(max_length=300)
    date_added = models.DateTimeField(default=timezone.now)

class Content(models.Model):
    """Content is an object that holds the paragraphs images and header of a page"""
    header = models.CharField(max_length=100)
    paragraphs = models.TextField(max_length=2000)
    image = models.ForeignKey(Image)

class Page(models.Model):
    """Page is an object that holds basic information about a single page"""
    title = models.CharField(max_length=30)
    content = models.ForeignKey(Content)
