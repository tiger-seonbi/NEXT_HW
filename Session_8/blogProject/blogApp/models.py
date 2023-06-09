from django.db import models

# Create your models here.
# 카테고리 추가
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content
    
class Reply(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replys')
    content = models.TextField()

    def __str__(self):
        return self.content

