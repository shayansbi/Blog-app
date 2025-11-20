from django.shortcuts import render
from django.views.generic import TemplateView 

from posts.models import Post




# class HomePageView(TemplateView):
#     model = Post
#     template_name = 'home.html'

def HomePageView(request):
    context = {
        'post' : Post.objects.all()
    }
        
    return render(request, 'home.html', context)

