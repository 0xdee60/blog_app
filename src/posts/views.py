from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Comment,Post,Like,PostView,User
from .forms import PostForm

class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context

