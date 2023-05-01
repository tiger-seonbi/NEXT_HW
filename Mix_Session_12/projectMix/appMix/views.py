from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Word, Item, Comment, Recomment
import random
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        exist_user = User.objects.filter(username=username)
        
        if exist_user:
            error = '이미 존재하는 유저입니다.'
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        
        return redirect('home')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('home')
        error = '아이디 또는 비밀번호가 틀립니다.'
        return render(request,'registration/login.html', {'error':error})
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    if request.method == 'POST':
        
        new_word = Word.objects.create(
            word = request.POST['word']
        )
        return redirect('home')
    words = Word.objects.all()

    return render(request, 'home.html', {'words':words})

#mix 할 때, 체크해주는 함수를 따로 빼서 정의한 것.
def is_valid(selected_new):
    items = list(Item.objects.all())
    legacy_list = []
    for element in items:
        temp=set()
        temp = set([element.word1, element.word2, element.word3])
        legacy_list.append(temp)
    print("레거시",legacy_list)
    if len(legacy_list):
        if selected_new in legacy_list:
            return True
        else:
            return False

# mix부분인데, 일단 워드에 들어가있는게 3개이상이면, 랜덤으로 3개 뽑아서 mixed_word에 넣어줘야하고,
# 그걸 아이템으로 매칭해야하는데 N:N 형태가 아니라 1:N 두개를 이어붙이는 형태로 해야 순서가 안꼬일 것 같기도하고?
# db 안에 있는 애들을 다 꺼내서 집합에 넣어주고 while문을 돌아갈 때, 체크를 해주는 느낌 체크 자체는 조합으로 그 수를 정해주고 연결된 함수가 뱉는 결과를 통해서 저장을 할지 샘플을 더 돌릴지 테스트하는 것.
@login_required(login_url="/registration/login/")
def mix(request):
    if request.method == 'POST':
        qswords = Word.objects.all()
        words = []
        for i in qswords:
            words.append(i.word)
        if len(words) >= 3:
            cnt = 0
            while True:
                cnt += 1
                random_selected = random.sample(words, 3)  
                selected_new = set(random_selected)
                if is_valid(selected_new):
                    if(cnt>=(len(words)* (len(words)-1) * (len(words)-2))/6):
                        print("이젠틀렸어")
                        break
                    else:
                        continue
                else:
                    print(selected_new)
                    new_mixed_word = Item.objects.create(
                    title = str(selected_new),
                    word1 = selected_new.pop(),
                    word2 = selected_new.pop(),
                    word3 = selected_new.pop(),
                    author = request.user,)
                    break
            items = Item.objects.all()
            return render(request, 'mix.html', {'items':items})
        else:
            return render(request, 'err.html')
    else:
        items = Item.objects.all()
        return render(request, 'mix.html', {'items':items})
                        
                #         new_mixed_word = Item.objects.create(
                # title =  ,
                # word1 = [0],
                # word2 = [1],
                # word3 = [2],)
                # break
        #         for a in mixed_word:
        #             testing_set.add(a)
                
        #         if test_set != testing_set:
        #             new_mixed_word = Item.objects.create(
        #         title = mixed_word,
        #         word1 = mixed_word[0],
        #         word2 = mixed_word[1],
        #         word3 = mixed_word[2],)
        #         break
        #     mixed_after_words = Item.objects.all()
        # mixed_list = []
        # return render(request, 'mix.html', {'mixed_after_words':mixed_after_words})
    # else:
    #     mixed_after_words = Item.objects.all()
    #     return render(request, 'mix.html',{'mixed_after_words':mixed_after_words, "error":"에러"})
    #     return render(request, 'mix.html', {'mixed_list':mixed_list})
        # if(len(mixed_words) == 0):
        #     new_mixed_word = Item.objects.create(
        #         title = mixed_word,
        #         word1 = mixed_word[0],
        #         word2 = mixed_word[1],
        #         word3 = mixed_word[2],
        #     )
        #     mixed_after_words = Item.objects.all()
        #     return render(request, 'mix.html', {'mixed_after_words':mixed_after_words})
        # else:
        #     return render(request, 'mix.html', {'mixed_list':mixed_list})
        
 
        # if len(words) >= 3:
        #     mixed_word = random.sample(mixed_list, 3)
        #     mixed_words = Item.objects.all()
        #     #중복 체크해야하는데 어떻게 하지..?
            
        #     print("\n\n\n")
        #     for item in mixed_words:
        #         test_list = [ item.word1.word, item.word2.word, item.word3.word]
        #         print(test_list)
        #         test_count = 0
        #         print("\n\n\n")
        #         for test_word in test_list:
        #             if test_word in mixed_word:
        #                 test_count += 1
        #                 print(test_count)
        #         if test_count !=3:
        #             new_mixed_word = Item.objects.create(
        #                 title = mixed_word,
        #                 word1 = mixed_word[0],
        #                 word2 = mixed_word[1],
        #                 word3 = mixed_word[2],
        #             )
        #             mixed_list = []
        #             return render(request, 'mix.html', {'mixed_words':mixed_words})
        #         else:
        #             return render(request, 'mix.html', 'mix.html',{"error":'에러'})
        # else:
        #     return redirect(request, 'mix.html')
# 에러 메시지용 함수
def err(request):
    return render(request, 'err.html')

# 디테일 함수, 댓글 기능 포함
@login_required(login_url="/registration/login/")
def detail(request, item_id):

    item = Item.objects.get(pk = item_id)
    if request.method == 'POST':
        Comment.objects.create(
            comment = request.POST['comment'],
            item = item,
            author = request.user,
        )
    comment = Comment.objects.filter(pk = item_id)

    return render(request, 'detail.html', {'item':item })

# 수정하기 함수
def update(request, item_id):

    item = Item.objects.get(pk = item_id)
    if request.method == "POST":
        Item.objects.filter(pk = item_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('detail', item_id)
    return render(request, 'update.html', {'item':item})

#삭제하기
def delete(request, item_id):
    
    item = Item.objects.get(pk = item_id)
    item.delete()

    return redirect('mix')

#댓글 삭제하기
def comment_delete(request, item_id, comment_id):

    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('detail', item_id)

#대댓글
def recomment(request, item_id, comment_id):

    item = Item.objects.get(pk = item_id)
    comment = Comment.objects.get(pk = comment_id)
    if request.method == 'POST':
        recomment = Recomment.objects.create(
            comment = comment,
            content = request.POST['content'],
        )
        return redirect('recomment', item_id, comment_id)
    return render(request, 'recomment.html', {'item':item, 'comment':comment})

#대댓글 삭제
def recomment_delete(request, item_id, comment_id, recomment_id):

    recomment = Recomment.objects.get(pk=recomment_id)
    recomment.delete()

    return redirect('detail', item_id)