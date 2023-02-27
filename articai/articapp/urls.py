from django.urls import path
from .import views


urlpatterns = [
    path('summarize/',views.summarize,name='summarize'),
    path('login/',views.loginuser,name='login'),
    path('',views.index,name='index'),
]