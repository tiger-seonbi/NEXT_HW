from django.contrib import admin
from .models import Article, Category
# Register your models here.
admin.site.register(Article)

class Category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, Category_admin)