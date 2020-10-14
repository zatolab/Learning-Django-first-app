from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Article


class ArticleView(View):

    def get(self, request):
        articles = Article.published.all()
        return render(request, 'blog/post/list.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, year, month, day, article):
        article = get_object_or_404(Article, url=article, status='published', publish__year=year, publish__month=month, publish__day=day)
        return render(request, 'blog/post/detail.html', {'article': article})
