
from django.shortcuts import render
from . models import people


# Create your views here.
def demo(request):
    obj = people.objects.all()

    return render(request,"index.html",{'result':obj})