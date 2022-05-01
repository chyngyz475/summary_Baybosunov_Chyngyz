import imp
from django.shortcuts import render

# Create your views here.
def all_blogs(request):
    Blogs = Blogs.objects.all()
    return render(request, 'blog/all_blogs.html')