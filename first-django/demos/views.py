from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calculator(request):
    # return HttpResponse("Started Calculator Func! Let's goooo!~~")
    return render(request, "calculator.html")
