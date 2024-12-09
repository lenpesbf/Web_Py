from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('login/', views.login_view),
    path('verify/', views.verify_view),
    path('error/', views.error_view),
    path('about-us/', views.about_us_view),
    path('checkout/', views.checkout_view), 
    path('compare/', views.compare_view),
    path('contact/', views.contact_view),
    path('faq/', views.faq_view), 
    path('payment/', views.payment_view), 
    path('shop-left-sidebar/', views.shop_left_sidebar_view), 
    path('cart/', views.cart_view),
    path('detail/', views.single_product_view),
    path('wishlist/', views.wishlist_view)
]