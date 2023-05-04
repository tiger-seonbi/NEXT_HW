from django.contrib import admin
from Blog.models import Post, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    # TabularInline은 같은 admin page에서 다른 model을 수정할 수 있는 권한을 부여한다. 
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')
    inlines = [ CommentInline ]
    search_fields = ['title', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)