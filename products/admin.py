from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Products)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')

admin.site.register(models.Category)
