from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 타이핑으로 넣을 수 받을 수 있는 데이터
class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word

# Word 데이터를 forein 으로 받아야하는 것 같은데, 이때 3개를 받아오려면 N:N 구조일 수 있겠다고 생각함.
# 이럴 필요 없이 word1, word2, word3를 모두 foreign key로 item 안에서 받는거임(gpt 아이디어)
# 안되는데? 오류 뜸.. 기본값으로 안넣어준게 있다는 오류 뱉는데 정신나가겠네
class Item(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    word1 = models.TextField()
    word2 = models.TextField()
    word3 = models.TextField()
    # word1 = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='item_word1', default=None)
    # word2 = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='item_word2', default=None)
    # word3 = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='item_word3', default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', null=True)
    def __str__(self):
        return self.title
#댓글
class Comment(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.comment
#대댓글
class Recomment(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content = models.TextField()

    def __self__(self):
        return self.content
