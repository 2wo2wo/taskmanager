from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Videos(models.Model):
    link  = models.CharField(max_length=255)
    video = models.TextField(default='')
    description = models.TextField()

class Program(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    videos = models.ManyToManyField(Videos, related_name='videos', blank=True)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE , blank=True)
    students_purchased = models.ManyToManyField(User, related_name='students', blank=True )

class Author(models.Model):
    t_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_programs = models.ManyToManyField(Program , related_name='programs_created', blank=True)
    is_active = models.BooleanField(default=False)
    is_declined = models.BooleanField(default=False)

class Student(models.Model):
    purchased_programs = models.ManyToManyField(Program , related_name='programs_purchased', blank=True)
    s_user = models.ForeignKey(User, on_delete=models.CASCADE)
    programs_selected = models.ManyToManyField(Program,related_name='selected_programs', blank=True)

class Stars(models.Model):
    comment  = models.CharField(max_length=255)
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_belong = models.ForeignKey(Program, on_delete=models.CASCADE)
    stars = models.IntegerField()


