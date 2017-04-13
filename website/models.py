from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    """Image is an object that holds the url and description of an image."""
    image = models.ImageField(upload_to="uploads/images")
    uploader = models.ForeignKey(User)
    description = models.TextField(max_length=300)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.image)

class Page(models.Model):
    """Page is an object that holds basic information about a single page"""
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    paragraphs = models.TextField(max_length=2000)
    image = models.ForeignKey(Image, null=True, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Person(models.Model):
    """Person represents client or user"""
    name = models.CharField(max_length=120)
    shortname = models.CharField(max_length=120, blank=True, null=True)
    short_description = models.CharField(max_length=60)
    photo = models.ForeignKey(Image)
    long_description = models.TextField()

    def __str__(self):
        return self.name +": "+self.short_description

class Organization(models.Model):
    """Organization is a client or partiner to ESDI."""
    name = models.CharField(max_length=120)
    photo = models.ForeignKey(Image)
    short_description = models.TextField(max_length=300)
    long_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name +": "+self.short_description

class Region(models.Model):
    """Region are places ESDI operates"""
    name = models.CharField(max_length=120)
    photo = models.ForeignKey(Image)
    short_description = models.TextField(max_length=300)
    long_description = models.TextField(max_length=1000)
