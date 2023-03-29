from django.shortcuts import render

def count(request):
    #logic here
    return render(request, 'count.html')

def result(request) :
    text = request.POST['text']
    total_len = len(text)
    no_space_len = len(text.replace(' ',''))
    word_count = len(text.split(' '))
    return render(request, 'result.html', {'total_len':total_len, 'text':text, 'no_space_len':no_space_len, 'word_count':word_count})