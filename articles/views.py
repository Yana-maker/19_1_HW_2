from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import ArticleForm
from .models import Article
from pytils.translit import slugify


# Create your views here.

class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('articles:list')
    permission_required = 'articles.add_article'
    extra_context = {
        'title': 'СОЗДАНИЕ СТАТЬИ'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Article
    form_class = ArticleForm
    permission_required = 'articles.view_article'
    extra_context = {
        'title': 'СТАТЬИ'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


    def random_articles(request):
        """чтобы вывести 3 случайные статьи """
        random_articles = Article.objects.order_by('?')[:3]
        return render(request, 'articles/article_list.html', {'random_articles': random_articles})


class ArticleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Article

    form_class = ArticleForm
    permission_required = 'articles.view_article'
    extra_context = {
        'title': 'ИНФО И СТАТЬЕ'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    permission_required = 'articles.change_article'
    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ СТАТЬИ'
    }

    def get_success_url(self):
        return reverse('articles:view', args=[self.object.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)



class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('articles:list')
    permission_required = 'articles.delete_article'
    extra_context = {
        'title': 'УДАЛЕНИЕ СТАТЬИ'
    }
