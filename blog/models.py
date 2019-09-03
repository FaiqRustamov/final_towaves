from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.

class Contactuser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    context = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Image = models.ImageField()
    Content = RichTextUploadingField(config_name='default')
    Tag = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=200, unique=True)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    def __unicode__(self):
        return u'%s' % self.Title
    
    class Meta:
        ordering = ('-Date',)

CATEGORY = (
    ('Music', 'Music'),
    ('Visual Arts', 'Visual Arts'),
    ('Film', 'Film'),
    ('Performing Arts', 'Performing Arts'),
    ('Lectures', 'Lectures'),
    ('Books', 'Books'),
    ('Food&Dring', 'Food&Dring'),
    ('Nightlife', 'Nightlife'),
)

class Category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='category')

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255, default=timezone.now())
    appointment_time = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='media/event')
    category = models.ForeignKey('Category',related_name='events',on_delete=models.CASCADE,null=True)

    user = models.ManyToManyField(User,related_name='events',blank=True)

    def __str__(self):
        return self.name

