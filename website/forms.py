from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<ul class="form-text text-muted"><li>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</li><li>Your username must be unique</li></ul>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.</span>'
        
# Create a form for the Record model       
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label = "")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label = "")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), label = "")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}), label = "")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), label = "")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), label = "")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), label = "")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}), label = "")
    
    class Meta:
        model = Record
        exclude = ('user',)    
        
    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].label = ''
        
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['phone'].label = ''
        
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].label = ''
        
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['city'].label = ''
        
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['state'].label = ''
        
        self.fields['zipcode'].widget.attrs['class'] = 'form-control'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
        self.fields['zipcode'].label = ''
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    