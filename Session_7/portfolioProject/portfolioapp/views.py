from django.shortcuts import render

# Create your views here.
def info(request):
    #no logic
    return render(request, 'info.html')