# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg fs-6',
        'placeholder': 'Tên đăng nhập'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg fs-6',
        'placeholder': 'Mật khẩu'
    }))

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg fs-6',
            'placeholder': 'Mật khẩu'
        })
    )
    password2 = forms.CharField(
        label="Xác nhận mật khẩu",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg fs-6',
            'placeholder': 'Xác nhận mật khẩu'
        })
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg fs-6',
                'placeholder': 'Tên đăng nhập'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg fs-6',
                'placeholder': 'Email'
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Tên đăng nhập đã tồn tại")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email đã tồn tại")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Mật khẩu không khớp")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        if len(password1) < 8:
            self.add_error('password1', "Mật khẩu phải có ít nhất 8 ký tự")
        return cleaned_data
