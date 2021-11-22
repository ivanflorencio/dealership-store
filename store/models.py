from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')    
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, )    
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255)
    costumer = models.ForeignKey('Costumer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name + ' ' + self.quantity

class Costumer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    def __str__(self):
        return self.name
        
class Cart(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return self.product.name + ' ' + self.quantity 

