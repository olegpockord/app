from django.urls import path

from treemenu import views

app_name = 'treemenu'

urlpatterns = [
    path('', views.MenuView.as_view(), name='index'),
    path('<slug:menu_slug>', views.MenuInfoView.as_view(), name='info'),
]