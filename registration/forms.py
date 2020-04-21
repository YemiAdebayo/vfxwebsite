from django import forms
from .models import Register

class RegistrationFormForAdmin(forms.ModelForm):
    """A form to give custom appearance to the registration table.
    """
    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'course')


class RegistrationFormForFrontend(forms.ModelForm):
    """A form to give custom appearance to the registration table.
    """

    COURSE_CHOICES = [
        ('CG Animation','CG Animation'),
        ('Film Making','Film Making'),
        ('Visual Effects','Visual Effects'),
        ]


    first_name = forms.CharField(
        max_length=100, label='Enter your first name:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler first_name home-address',
                'placeholder': 'First name',
                'name': 'first_name'
            }
        ))
    last_name = forms.CharField(
        max_length=100, label='Enter your last name:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler last_name',
                'placeholder': 'Last name',
                'name': 'last_name'
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
    
    course = forms.CharField(
        required=True,
        label="Select A Course",
        widget=forms.Select (choices=COURSE_CHOICES,
        attrs={
            'name': 'course',
            "class" : 'select-error-handler custom-select',
        }),
    )

    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'course')

    def clean_first_name(self):
        # Clean first_name
        first_name = self.cleaned_data.get("first_name")
        return first_name

    def clean_last_name(self):
        # Clean first_name
        last_name = self.cleaned_data.get("last_name")
        return last_name

    def clean_phone_number(self):
        # Clean first_name
        phone_number = self.cleaned_data.get("phone_number")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_course(self):
        # Clean first_name
        course = self.cleaned_data.get("course")
        return course