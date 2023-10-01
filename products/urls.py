# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:product_id>/', views.product_update, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete, name='product_confirm_delete'),

]
