from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import User
from .models import Customer, Product
from .models import Service
from .models import Customer, Service


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 'city', 'state', 'zipcode', 'email','phone_number')
class ServiceForm(forms.ModelForm):
   class Meta:
       model = Service
       fields = ('cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time', 'service_charge' )

class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ('cust_name','product', 'p_description', 'quantity', 'pickup_time', 'charge' )


# from django.contrib.auth.forms import UserCreationForm
# from .models import User
#
#
# class UserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('username', 'email', 'employee_cell_phone')
#
# class UserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'department', 'employee_cell_phone')


