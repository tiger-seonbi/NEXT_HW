from django.shortcuts import render, redirect
from .models import Article, Category
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

    return render(request, 'detail.html', {'article':article})

def board(request, board_name):
    # category_name = request.GET.get('category')
    # # category_name = request.POST['category']
    # print(category_name)
    cate = Category.objects.get(name=board_name)

    filter_cat = Article.objects.filter(category=cate)

    return render(request, 'board.html', {'filter_cat':filter_cat, 'cate':cate})