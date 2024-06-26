
from .models import Product, Wishlist
from django import forms
from .models import User,Profile,Category


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_dealer = forms.BooleanField(label='Are you a dealer?',required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer']
        help_texts={'username':''}
       
        

    def clean(self):
        cleaned_data = super().clean()
        is_dealer = cleaned_data.get('is_dealer')
        dealer_details = cleaned_data.get('dealer_details')

        # if is_dealer and not dealer_details:
        #     raise forms.ValidationError('Dealer details are required for dealer registration')

        return cleaned_data
    
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity','price', 'image','category']




class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = []



class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label='Quantity')

class profileform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        help_texts={'username':''}






class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        labels = {
            'name': 'Category Name',
        }