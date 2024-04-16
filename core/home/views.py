from django.shortcuts import render, redirect
from django.views.generic import View
from home.models import Post
from django.utils.translation import activate

class HomeView(View):
    def get(self, request):
        post = Post.objects.filter(status='p', show=True)
        return render(request, 'home/home.html', {'post': post})
    
    
class ChangLang(View):
    def get(self, request):
        activate(request.GET.get('lang'))
        return redirect(request.GET.get('next'))