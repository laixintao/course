#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )

    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm,self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )

    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )
    password_chk = forms.CharField(
            required=True,
            label=u'确认密码',
            error_messages={'required':u'请再一次输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u'确认密码',
                }
            )
    )

    jobnum = forms.IntegerField(
        required=False,
        label="工号",
        widget=forms.NumberInput(
            attrs={
                'placeholder':u'6位工号'
            }
        )
    )

    email = forms.EmailField(
        required=False,
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'placeholder':u'请输入合法的邮件地址'
            }
        )
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        elif self.cleaned_data['password'] != self.cleaned_data['password_chk']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(RegisterForm,self).clean()
        return cleaned_data