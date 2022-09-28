from pipes import Template
from django.urls import path
from . import views


urlpatterns = [
  # employee
  path('employee/', views.index, name='employee'),
  path('create/', views.create, name='create'),
  path('create/create_data/', views.create_data, name='create_data'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('update/<int:id>/', views.update, name='update'),
  path('update/update_data/<int:id>/', views.update_data, name='update_data'),
  # blog
  path('', views.blog, name='blog'),
  path('detail/<int:id>/', views.detail_page, name='detail'),
]