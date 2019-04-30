from django.contrib import admin

from .models import Write


# Register your models here.

class BappOptions(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created']


admin.site.register(Write, BappOptions)
