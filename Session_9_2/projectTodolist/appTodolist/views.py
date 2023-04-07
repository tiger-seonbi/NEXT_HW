from django.shortcuts import render, redirect
from .models import Todolist, Doornot
# Create your views here.
def home(request):

    tasks = Todolist.objects.all().order_by('due_date')
    
    return render(request, 'home.html',{'tasks':tasks} )

def new(request):
    #일단 if 구문이용해서 요청 받았을 때
    if request.method == 'POST':

        #doornot을 요청을 받고, 그 변수와 같은걸 모델에서 찾아서 Todolist 모델에서 다시 불러오는 것!
        condition = request.POST['doornot']
        now_condition = Doornot.objects.get(state = condition)

        new_todo = Todolist.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            due_date = request.POST.get('due_date'),
            to_day = request.POST.get('to_day'),
            doornot = now_condition
            )

        return redirect('home')
    doornot_list = Doornot.objects.all()

    return render(request, 'new.html', {'doornot_list':doornot_list} )

def details(request, todo_pk):

    task = Todolist.objects.get(pk = todo_pk)

    return render(request, 'details.html', {'task':task})

def update(request, todo_pk):

    task = Todolist.objects.get(pk = todo_pk)

    if request.method == 'POST':
        condition = request.POST['doornot']
        now_condition = Doornot.objects.get(state = condition)

        new_todo = Todolist.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            detail = request.POST['detail'],
            due_date = request.POST['due_date'],
            to_day = request.POST.get('to_day'),
            doornot = now_condition,
        )
        return redirect('/home/',todo_pk)
    
    doornot_list = Doornot.objects.all()

    return render(request, 'update.html', {'task':task,'doornot_list':doornot_list})
    
def delete(request, todo_pk):

    task = Todolist.objects.get(pk = todo_pk)
    task.delete()

    return redirect('/home/')