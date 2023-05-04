from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

class CreateUserForm(UserCreationForm):
    class Meta:
        model=Profile
        fields = ['username', 'email', 'age', 'password1', 'password2']

def signup(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:home')
        else:
            error = '정보가 유효하지 않습니다.'
            return render(request, 'accounts/signup.html', {'error':error})
    return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET.get('next', '/'))
            else:
                return redirect('Blog:home')
        else:
            error = '아이디 또는 비밀번호가 틀립니다.'
            return render(request, 'accounts/login.html', {'error':error})
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('Blog:home')