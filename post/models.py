from django.db import models
import jdatetime
from django_jalali.db import models as jalali_models
from django.contrib.auth.models import User
from . import validatorFile
# Create your models here.
"""
this place we create models for posts and cattegory for every post
"""
class Categorie(models.Model):
    name = models.CharField(max_length=100,default='',null=False,blank=False)
    def __str__(self):
        return f'{self.name}'
class post(models.Model):
    title = models.CharField(max_length=100,default='',null=False,blank=False)
    #author = models.CharField(max_length=100,default='',null=False,blank=False)
    content = models.TextField(default='',null=True,blank=True)

    image = models.ImageField(upload_to='media/post/',default='default.jpg')
    pub_date = jalali_models.jDateTimeField()
    category = models.ManyToManyField(Categorie)
    def __str__(self):
        return f'{self.title} , {self.pub_date}'
class largeContent(models.Model):
    post = models.ForeignKey('post', on_delete=models.CASCADE)
    content = models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return f'{self.content}'
class ImageCollection(models.Model):
    post = models.ForeignKey('post',on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to='media/postCollection/',default='default.jpg')


#this place you can create custom user models for every post for every category and create assiciated model for every post
class user(models.Model):
    name = models.CharField(max_length=100,default='',null=False,blank=False)
    family=models.CharField(max_length=100,default='',null=False,blank=False)
    password = models.CharField(max_length=100,default='',null=False,blank=False)
    email = models.CharField(max_length=100,default='',null=False,blank=False)
    image = models.ImageField(upload_to='media/user/',default='default.jpg')
    studentCode=models.CharField(default=0,null=False,blank=False,max_length=12,validators=[validatorFile.validate_No_Alphabet])
    admin=models.BooleanField(default=False)
    teacher=models.BooleanField(default=False)
    ForumsMember=models.BooleanField(default=False)
    title=models.CharField(max_length=100,default='')
    bio=models.CharField(max_length=500,default='')
    def __str__(self):
        return f'{self.name}'

"""
class comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.text}'

"""


class videoclass(models.Model):
    name = models.CharField(max_length=100,default='',null=False,blank=False)
    cover = models.ImageField(upload_to='media/videoclass/',default='default.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=100,default='',null=False,blank=False)
    largeContent= models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return f'{self.name}'

class comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.text}'
class Certificate(models.Model):
    title = models.CharField(max_length=100,default='',null=False,blank=False)
    description = models.TextField(default='',null=True,blank=True)
    image = models.ImageField(upload_to='media/certificate/',default='default.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'