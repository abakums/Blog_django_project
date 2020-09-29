from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_last_articles, name='show_last_articles'),
    path('all_articles/', views.show_all_articles, name='show_all_articles'),
    path('category/<int:category_id>/', views.show_category_articles, name='show_category_articles'),
    path('article/<int:article_id>/', views.show_article, name='show_article')
]