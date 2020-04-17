from django.shortcuts import render

def index(request):
    context={'text':"hello world", 'number':100, 'date':'2020-04-16'}
    return render(request,'basic_app/index.html', context)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
