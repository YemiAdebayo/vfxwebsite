from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users information. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'text-input error-handler password',
            'placeholder': 'Provide password for this account',
            'name': 'Password'
        }
    ), label='Enter password:')
    password2 = forms.CharField(
        label='Confirm your password:', widget=forms.PasswordInput(
            attrs={
                'class': 'text-input error-handler password',
                'placeholder': 'Confirm the password above',
                'name': 'Confirm password'
            }
        ))
    first_name = forms.CharField(
        max_length=100, label='Enter your first name:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler first_name home-address',
                'placeholder': 'First name',
                'name': 'first name'
            }
        ))
    last_name = forms.CharField(
        max_length=100, label='Enter your last Name:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler last_name',
                'placeholder': 'Last name'
            }
        ))
    phone_number = forms.CharField(
        max_length=100, label='Enter your phone number:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler phone-number',
                'name': 'last name',
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

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is taken!")
        return email

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

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match!")
        else:
            try:
                validate_password(self.cleaned_data["password"])
            except ValidationError as e:
                raise forms.ValidationError(e)
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)

        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
