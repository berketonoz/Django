from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('date', view=views.get_date, name='date'),
]
