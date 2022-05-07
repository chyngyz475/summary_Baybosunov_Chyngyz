from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import News

# Create your views here.
def News (request):
    projects = News.objects.all()
    return render(request, 'portfolio/base.html',{'projects':projects})
