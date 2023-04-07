from django.db import models

# Create your models here.
# To do list의 타이틀, 디테일, due-date, 완료/미완료 를 포함한 model 생성
class Todolist(models.Model):
    title = models.CharField(max_length=20)
    detail = models.TextField()
    due_date = models.DateField('DUE_DATE', blank=True, null=True)
    to_day = models.DateField(auto_now = True, null=True)
    doornot = models.ForeignKey('Doornot',on_delete=models.CASCADE, blank=True, null=True )
    
    def __str__(self):
        return self.title
    
# To do list에서 완료/미완료 체크하기 위한 model 생성
class Doornot(models.Model):
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state