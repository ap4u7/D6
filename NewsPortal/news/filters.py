import django_filters
from django_filters import FilterSet
from .models import *
from django import forms



# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title',
                                      label='В названии:',
                                      lookup_expr='icontains', )
    author = django_filters.CharFilter(field_name='author__user__username',
                                       label='По автору:',
                                       lookup_expr='icontains', )
    created = django_filters.DateFilter(field_name='created',
                                             label='Начиная с даты:',
                                             widget=forms.DateInput(attrs={"type": "date"}),
                                             lookup_expr='date__gte', )
