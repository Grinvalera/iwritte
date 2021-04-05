from django.urls import path

from .views import one_page, second_page, third_page, main_page

urlpatterns = [
    path('', one_page, name='one_page'),
    path('second', second_page),
    path('third', third_page),
    path('redirect', main_page, name='redirect')
]