from django.shortcuts import render

# Create your views here.



def category(request):
    return render(request, 'category.html')

def manage(request):
    return render(request, 'manage.html')
def manageview(request):
    return render(request, 'manageview.html')


def categoryview(request):
    return render(request, 'categoryview.html')


def blog(request):
    return render(request, 'blog.html')


def blogview(request):
    return render(request, 'blogview.html')

def login(request):
    return render(request, 'login.html')