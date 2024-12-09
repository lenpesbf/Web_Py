from django.shortcuts import render

#home
def home_view(request):
    return render(request, 'app/index.html')

#view login
def login_view(request):
    return render(request, 'app/login-register.html')

#verify
def verify_view(request):
    return render(request, 'app/verify.html')

#checkout
def checkout_view(request):
    return render(request, 'app/checkout.html')

#404html
def error_view(request):
    return render(request, 'app/404.html')

#about us page
def about_us_view(request):
    return render(request, 'app/about-us.html')

#compare page
def compare_view(request):
    return render(request, 'app/compare.html')

#contact page
def contact_view(request):
    return render(request, 'app/contact.html')

#faq page
def faq_view(request):
    return render(request, 'app/faq.html')

#payment page
def payment_view(request):
    return render(request, 'app/payment.html')

#shop left sidebar page
def shop_left_sidebar_view(request):
    return render(request, 'app/shop-left-sidebar.html')

#shopping cart page
def cart_view(request):
    return render(request, 'app/shopping-cart.html')

#single-product page
def single_product_view(request):
    return render(request, 'app/single-product.html')

#wishlist page
def wishlist_view(request):
    return render(request, 'app/wishlist.html')