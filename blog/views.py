# from django.shortcuts import render, get_object_or_404
from .models import Blog, CategoryPost
from django.views.generic import ListView, DetailView


class PostsList(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = CategoryPost.objects.all()
        context['category_selected'] = 0
        return context
    
    def get_queryset(self):
        return Blog.objects.filter(publish=True)


class PostDetail(DetailView):
    model = Blog
    template_name = 'blog/showpost.html'
    context_object_name = 'detail_post'


class PostsByCategory(ListView):
    model = CategoryPost
    template_name = "blog/blog_list.html"
    # allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = CategoryPost.objects.all()
        return context

    def get_queryset(self):
        return Blog.objects.filter(category__slug=self.kwargs['slug'], publish=True)
