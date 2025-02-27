from django import forms
from.models import customuser

class userform(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput
                                (attrs={'class':'form-control','placeholder':'Enter first name','max_length':100}))
    last_name = forms.CharField(widget=forms.TextInput
                                (attrs={'class':'form-control','placeholder':'Enter last name','max_length':100}))
    email = forms.CharField(widget=forms.TextInput
                                (attrs={'class':'form-control','placeholder':'Enter email','max_length':100}))
    password = forms.CharField(widget=forms.TextInput
                                (attrs={'class':'form-control','placeholder':'Enter Password','max_length':100}))
    address = forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control','placeholder':'Enter address','max_length':100}))
    phone_number = forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control','placeholder':'Enter Phone number','max_length':20}))
    user_profile = forms.ImageField()

    class Meta:
        model = customuser
        fields = ('first_name','last_name','email','password','address','phone_number','user_profile')
