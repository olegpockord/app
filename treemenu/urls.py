from django.urls import path

from treemenu import views

app_name = 'treemenu'

urlpatterns = [
    path('', views.MenuView.as_view(), name='index')
]