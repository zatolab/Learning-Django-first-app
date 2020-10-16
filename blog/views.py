from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


class ArticleView(View):

    def get(self, request):

        object_list = Article.published.all()
        paginator = Paginator(object_list, 3)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        return render(request, 'blog/articles/list.html', {'page': page, 'articles': articles})

        #articles = Article.published.all()
        #return render(request, 'blog/articles/list.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, year, month, day, article):
        article = get_object_or_404(Article, url=article, status='published', publish__year=year, publish__month=month, publish__day=day)
        return render(request, 'blog/articles/detail.html', {'article': article})
