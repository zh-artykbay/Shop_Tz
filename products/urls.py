from django.urls import path
from products.views import ProductList, ProductDetail


urlpatterns = [
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('products', ProductList.as_view()),
]
