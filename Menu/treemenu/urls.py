from django.urls import path
from .views import *


app_name = 'treemenu'

urlpatterns = [
    path('menu/', MenuPageView.as_view(), name='index'),
]