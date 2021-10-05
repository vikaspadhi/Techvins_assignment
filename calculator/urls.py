from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('submit',views.evaluate , name='submitquery'),
]
