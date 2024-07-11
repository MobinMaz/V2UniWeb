from django.contrib import admin
from . import models
# Register your models here.
class PostImage(admin.TabularInline):
    model = models.ImageCollection
    extra = 1
class Certification(admin.TabularInline):
    model = models.Certificate
    extra = 1
@admin.register(models.post)
class postAdmin(admin.ModelAdmin):
    inlines = [PostImage]
@admin.register(models.user)
class userAdmin(admin.ModelAdmin):
    inlines = [Certification]


admin.site.register(models.comment)

admin.site.register(models.Categorie)
admin.site.register(models.videoclass)
