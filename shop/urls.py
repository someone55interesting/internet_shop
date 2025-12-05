from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Главная страница (все товары)
    path('', views.product_list, name='product_list'),
    # Товары по категории (например, /electronics/)
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # Страница одного товара (например, /1/iphone-15/)
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]