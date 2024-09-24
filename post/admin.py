from django.contrib import admin
from . import models
from django.contrib.auth.models import User
admin.site.unregister(User)
# Register your models here.
class PostImage(admin.TabularInline):
    model = models.ImageCollection
    extra = 1
class Certification(admin.TabularInline):
    model = models.Certificate
    extra = 1
class largeContent(admin.TabularInline):
    model = models.largeContent
    extra = 1
@admin.register(models.post)
class postAdmin(admin.ModelAdmin):
    inlines = [PostImage,largeContent]
@admin.register(models.user)
class userAdmin(admin.ModelAdmin):
    list_display = ('name','family','email', 'studentCode')
    inlines = [Certification]


admin.site.register(models.comment)

admin.site.register(models.Categorie)
admin.site.register(models.videoclass)
