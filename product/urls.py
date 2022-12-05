from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [ 
    # ================================ PRODUCT ================================
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/new/', views.ProductCreateView.as_view(), name='product_new'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    
    # ================================ CART ================================
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart/new/', views.CartCreateView.as_view(), name='cart_new'),
    path('cart/detail/<int:pk>/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/update/<int:pk>/', views.CartUpdateView.as_view(), name='cart_update'),
    path('cart/delete/<int:pk>/', views.CartDeleteView.as_view(), name='cart_delete'),
    
    path('cart/finalize_purchase/', views.finalize_purchase, name='finalize_purchase'),
]