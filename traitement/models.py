from django.db import models
from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

class Question(models.Model):
    TYPES = (
        ('backend','backend'),
        ('frontend','frontend'),
        ('fullstack','fullstack')
    )
    
    reponse = models.CharField(max_length=200, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.title


class skill(models.Model):
    title =models.CharField(max_length=200)
    logo = models.ImageField(null=True )
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    nom =models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.nom

class Message(models.Model):
    nom = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)   
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.nom
    
class Endocement(models.Model):
    nom = models.CharField(max_length=200, null=True)
    body = models.TextField()
    approuvé = models.BooleanField(default=False, null=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body[0:50]
    
class comment(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.body[0:50]

