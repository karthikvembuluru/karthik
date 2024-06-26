from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dealer_details = models.CharField(max_length=100, blank=True, null=True)

    class Role(models.TextChoices):
        USERS = 'users', 'Users' 
        DEALER = 'dealer', 'Dealer'
        ADMIN = 'admin','Admin'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USERS)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=300,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name
    




class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.product.name}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
