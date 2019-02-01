from django.shortcuts import render

# Create your views here.


def fontend(request):
    return render(request, 'fn_index.html')



def contact(request):
    return render(request, 'contact.html')



def term(request):
    return render(request, 'terms.html')