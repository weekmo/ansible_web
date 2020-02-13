from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .apps import AnsibleWebConfig

from . import views

app_name = 'ansible_web'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('hosts/', views.hosts, name='hosts'),
    path('get_playbook/<int:pk>', views.get_playbook, name='get_playbook'),
    path('delete_playbook/<int:pk>', views.delete_playbook, name='delete_playbook'),
    path('playbook/add/', login_required(views.PlaybookCreate.as_view()), name='playbook-add'),
    path('playbook/edit/<int:pk>', login_required(views.PlaybookUpdate.as_view()),name='playbook-edit'),
    #path('playbook/delete/<int:pk>', login_required(views.PlaybookDelete.as_view()),name='playbook-delete'),
]
