from django.shortcuts import render

# Create your views here.
def landing_page(request):
    context={}
    return render(request, 'home.html', context)