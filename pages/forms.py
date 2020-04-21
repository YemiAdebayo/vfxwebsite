from django import forms
from .models import CustomerInquiry


class CustomerInquiryFormForAdmin(forms.ModelForm):

    """A form to give custom appearance to the registration table.
    """

    full_name = forms.CharField(
        max_length=100, label='Enter your full name:', widget=forms.TextInput(
            attrs={

                'class': 'text-input error-handler first_name home-address',
                'placeholder': 'First name',
                'name': 'first_name'
            }
        ))

    phone_number = forms.CharField(
        max_length=100, label='Enter your phone number:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler phone-number',
                'name': 'phone_number',
                'placeholder': 'E.g 080XXXXXXXX',
                'pattern': r'^[0][8]\d{9}$|^[0][7]\d{9}$|^[0][9]\d{9}$|^[\+][2][3][4][7]\d{9}$|^[\+][2][3][4][8]\d{9}$|^[\+][2][3][4][9]\d{9}$|^[2][3][4][7]\d{9}$|^[2][3][4][8]\d{9}$|^[2][3][4][9]\d{9}$'
            }
        ))

    email = forms.EmailField(
        max_length=100, label='Enter your email:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler email',
                'placeholder': 'example@mymail.com',
                'name': 'email',
            }
        ))

    message = forms.CharField(
        max_length=100, label='Enter your inquiry:', widget=forms.Textarea(
            attrs={
                'class': 'text-input error-handler message',
                'name': 'phone_number',
                'placeholder': 'Enter your inquiry in this box',
            }
        ))

    class Meta:
        model = CustomerInquiry
        fields = ('full_name', 'phone_number', 'email', 'message')


class CustomerInquiryForm(forms.ModelForm):
    """A form to give custom appearance to the registration table.
    """

    full_name = forms.CharField(
        max_length=100, label='Enter your full name:', widget=forms.TextInput(
            attrs={

                'class': 'text-input error-handler first_name home-address',
                'placeholder': 'First name',
                'name': 'first_name'
            }
        ))

    phone_number = forms.CharField(
        max_length=100, label='Enter your phone number:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler phone-number',
                'name': 'phone_number',
                'placeholder': 'E.g 080XXXXXXXX',
                'pattern': r'^[0][8]\d{9}$|^[0][7]\d{9}$|^[0][9]\d{9}$|^[\+][2][3][4][7]\d{9}$|^[\+][2][3][4][8]\d{9}$|^[\+][2][3][4][9]\d{9}$|^[2][3][4][7]\d{9}$|^[2][3][4][8]\d{9}$|^[2][3][4][9]\d{9}$'
            }
        ))

    email = forms.EmailField(
        max_length=100, label='Enter your email:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler email',
                'placeholder': 'example@mymail.com',
                'name': 'email',
            }
        ))

    message = forms.CharField(
        max_length=100, label='Enter your inquiry:', widget=forms.Textarea(
            attrs={
                'class': 'text-input error-handler message',
                'name': 'phone_number',
                'placeholder': 'Enter your inquiry in this box',
            }
        ))

    class Meta:
        model = CustomerInquiry
        fields = ('full_name', 'phone_number', 'email', 'message')

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_message(self):
        message = self.cleaned_data.get("message")
        return message
