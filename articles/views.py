from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    article_object = Article.objects.all()
    articles = article_object.order_by('-published_at')
    # scopes = Article.scopes.all()
    # scopes = scope_object.order_by('-topic')
    # context = {'articles': articles}
    context = {'articles': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)
