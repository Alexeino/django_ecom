from django.urls import path
from .views import ProductAV, ProductDetailsAV

urlpatterns = [
    path('all/',ProductAV.as_view(),name="products_av"),
    path('id/<int:pk>/',ProductDetailsAV.as_view(),name="product_details")
]
