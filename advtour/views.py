from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'advtour/index.html')

def about(request):
    return render(request,'advtour/about.html')


def gridview(request):
    return render(request,'advtour/grid.html', context={})