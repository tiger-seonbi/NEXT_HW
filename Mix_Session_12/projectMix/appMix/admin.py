from django.contrib import admin
from .models import Word, Item, Comment, Recomment
# Register your models here.

admin.site.register(Word)
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Recomment)