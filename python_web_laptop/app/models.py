from django.db import models

#Create Tabel Into SQLITE
#Table Company hãng sản xuất
class Company(models.Model):
    id_company = models.CharField(max_length=255, primary_key=True)
    name_company = models.CharField(max_length=255)

#Table category
class Category(models.Model):
    category_id = models.CharField(max_length=255, primary_key=True)
    category_name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

#Table product
class Product(models.Model):
    product_id = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product_id', 'category', 'company')

#
class StockReceipt(models.Model):
    stock_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    receipt_date = models.DateTimeField()
    supplier = models.CharField(max_length=255, null=True, blank=True)
    unit_cost = models.FloatField()

    class Meta:
        unique_together = ('stock_id', 'product')


class Inventory(models.Model):
    inventory_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('inventory_id', 'product')


class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)


class ShoppingCart(models.Model):
    cart_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('cart_id', 'user')


class ShoppingCartDetail(models.Model):
    cartdt_id = models.CharField(max_length=255)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('cartdt_id', 'cart', 'product')


class Order(models.Model):
    order_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.FloatField()

    class Meta:
        unique_together = ('order_id', 'user')


class Payment(models.Model):
    pay_id = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=50)

    class Meta:
        unique_together = ('pay_id', 'order')


class PaymentMethod(models.Model):
    paymethod_id = models.CharField(max_length=255)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    method_name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('paymethod_id', 'payment')


class OrderDetail(models.Model):
    orderdt_id = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('orderdt_id', 'order', 'product')


class Role(models.Model):
    role_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('role_id', 'user')


class Address(models.Model):
    address_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        unique_together = ('address_id', 'user')    
