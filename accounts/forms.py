from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
# এটি বেস্ট প্র্যাকটিস
User = get_user_model()
# from django.contrib.auth.models import User
# এটি Django এর ডিফল্ট User মডেল
# সরাসরি User মডেলকে ইমপোর্ট করে
# যদি আপনি কাস্টম User মডেল ব্যবহার করেন, তাহলে এই পদ্ধতি সমস্যা তৈরি করতে পা
class SignInForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username or Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})

    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'confirm_password': 'Confirm Password'
        }
        for field, placeholder in placeholders.items():
            self.fields[field].widget.attrs.update({'placeholder': placeholder})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'placeholder': 'Current Password',
            'class': 'input-field'
        })
        self.fields['new_password1'].widget.attrs.update({
            'placeholder': 'New Password',
            'class': 'input-field'
        })
        self.fields['new_password2'].widget.attrs.update({
            'placeholder': 'Confirm New Password',
            'class': 'input-field'
        })
