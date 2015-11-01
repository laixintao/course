#coding=utf-8
from django import forms
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput
import time

class courseForm(forms.Form):
    course_name = forms.CharField(
        required = True,
        label=u"课程名称",
        error_messages={'required':'请输入课程名称'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"课程名称",
            }
        )
    )
    time = forms.DateTimeField(
        required=True,
        label=u"预约时间",
        error_messages={'required':'请输入可预约时间'},
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={
                'placeholder':u'年-月-日 时：分'
            }
        ),
        initial=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
    )
    room = forms.CharField(
        required=True,
        label=u"地点",
        error_messages={'required':"请输入地点"},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'教学楼，教室号等'
            }
        )
    )
    max_people = forms.CharField(
        required=False,
        label=u'最大人数',
        widget=forms.NumberInput(
            attrs={
                'placeholder':u' 最大人数',
                'default':100,
            }
        ),
        initial=100
    )


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"需要填写更多信息！")
        else:
            cleaned_data = super(courseForm,self).clean()