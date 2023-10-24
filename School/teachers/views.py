from django.shortcuts import render

# Create your views here.
def teach(request):
    return render(request, 'teach.html')