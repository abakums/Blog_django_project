from django.shortcuts import render
from .models import Article, Category


def show_last_articles(request):
    params = dict()
    params['articles'] = Article.objects.order_by('-id')[0:6]
    params['categories'] = Category.objects.all()
    return render(request, 'main_page.html', params)


def show_all_articles(request):
    params = dict()
    params['articles'] = Article.objects.all()
    params['categories'] = Category.objects.all()
    return render(request, 'all_articles.html', params)


def show_category_articles(request, category_id):
    params = dict()
    params['articles'] = Article.objects.filter(category=category_id)
    params['categories'] = Category.objects.all()
    params['category'] = Category.objects.get(id=category_id)
    return render(request, 'category_articles.html', params)


def show_article(request, article_id):
    params = dict()
    params['article'] = Article.objects.get(id=article_id)
    params['categories'] = Category.objects.all()
    return render(request, 'article.html', params)
