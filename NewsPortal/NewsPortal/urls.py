from django.contrib import admin
from django.urls import path
from news.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', NewsCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', NewsDelete.as_view(), name='article_delete'),


]
