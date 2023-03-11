from django.contrib import admin
from django.urls import path
from news.views import NewsList, NewsDetail


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news'),

]
