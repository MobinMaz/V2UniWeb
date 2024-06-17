from django.contrib import admin
from . import models
# Register your models here.
class PostImage(admin.TabularInline):
    model = models.ImageCollection
    extra = 3
@admin.register(models.post)
class postAdmin(admin.ModelAdmin):
    inlines = [PostImage]



admin.site.register(models.comment)
admin.site.register(models.user)
admin.site.register(models.category)
admin.site.register(models.videoclass)
