from django.shortcuts import render, redirect
from .models import Article, Category, Comment, Reply
# Create your views here.
def new(request):
    if request.method == 'POST':

        print(request.POST) #출력 형태 보여주기 위함
        
        #카테고리 인스턴스 가져와야함.
        category_name = request.POST['category']
        cate = Category.objects.get(name=category_name)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = cate
        )
        
        return redirect('home')
    categories = Category.objects.all()

    return render(request, 'new.html', {'categories':categories})

def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    return render(request, 'home.html', {'articles':articles, 'categories':categories})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':


        Comment.objects.create(
            content = request.POST['content'],
            article = article
        )

        return redirect('detail', article_id)

    return render(request, 'detail.html', {'article':article})

def comment_delete(request, comment_pk, article_id):
    comment = Comment.objects.get(id=comment_pk)
    comment.delete()

    return redirect('detail', article_id)

#논리구조 싹다 뜯고 + url 매핑도 다시해야함.
def reply(request, comment_pk, article_id):

    article = Article.objects.get(id=article_id)
    # 여기서 코멘트 중에 아티클 해당 아티클 아이디 있는거 가져오는 방법, 리플 중에 해당 코멘트 중에 있는거 가져오는 방법 찾아야함.
    comment = Comment.objects.filter(article = article)
    this_comment = Comment.objects.get(pk = comment_pk)
    replies = Reply.objects.filter(comment = this_comment)
    if request.method == 'POST':
        Reply.objects.create(
            content = request.POST['content'],
            comment = this_comment
        )
        return redirect('reply', article_id, comment_pk)
    return render(request, 'reply.html', {'article':article, 'comment':comment, 'replies':replies})

def reply_delete(request, comment_pk, article_id, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    reply.delete()

    return redirect('reply', article_id, comment_pk)


def board(request, board_name):
    # category_name = request.GET.get('category')
    # # category_name = request.POST['category']
    # print(category_name)
    cate = Category.objects.get(name=board_name)

    filter_cat = Article.objects.filter(category=cate)

    return render(request, 'board.html', {'filter_cat':filter_cat, 'cate':cate})