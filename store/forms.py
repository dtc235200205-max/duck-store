from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập'}),
        }
        labels = {
            'first_name': 'Tên',
            'last_name': 'Họ',
            'email': 'Email',
            'username': 'Tên đăng nhập',
        }

class UserProfileExtendedForm(forms.ModelForm):
    """Form để chỉnh sửa thông tin mở rộng của người dùng"""
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'avatar']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ', 'rows': 3}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ',
            'avatar': 'Ảnh đại diện',
        }