from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import generic
from .forms import PhotoForm
from .models import PhotoModel

from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404


from mediasite.models import Post, Category, Tag


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class IndexView(ListView):
    model = Post
    template_name = 'mediasite/index.html'


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))



class CategoryPostView(ListView):
    model = Post
    template_name = 'mediasite/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostView(ListView):
    model = Post
    template_name = 'mediasite/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class Photo(generic.CreateView):
    model = PhotoModel
    form_class = PhotoForm
    template_name = 'mediasite/upload.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Photo, self).get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["photos"] = PhotoModel.objects.all()
        return context