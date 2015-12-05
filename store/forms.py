#coding=utf-8
from django import forms
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput
import time
from models import Item

def get_items():
    items = Item.objects.all()
    result = []
    for i in items:
        result.append((str(i),str(i)))
        print i
    print result
    return result

class NewItemForm(forms.Form):

    iid = forms.IntegerField(
        required=True,
        label=u'商品编号',
        widget=forms.TextInput()
    )
    name = forms.CharField(
        required = True,
        label=u"货物名称",
        error_messages={'required':'请输入货物名称'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"货物名称",
            }
        )
    )

    price = forms.IntegerField(
        required=True,
        label=u'价格',
        widget=forms.TextInput()
    )



    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"需要填写更多信息！")
        else:
            cleaned_data = super(NewItemForm,self).clean()

class IncomeForm(forms.Form):
    account_type=forms.ChoiceField(
        label=u'商品种类',
        required=True,
        choices=get_items(),
        widget=forms.RadioSelect())

    # item = forms.RadioChoiceInput(
    #     required=True,
    #     label=u'货物名称',
    #     widget=forms.RadioSelect(
    #         choices=('none','one',)
    #     )
    # )

    num = forms.IntegerField(
        required=True,
        label=u'入库数量',
        widget=forms.TextInput(

        )
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"需要填写更多信息！")
        else:
            cleaned_data = super(IncomeForm,self).clean()


class OutcomeForm(forms.Form):
    account_type=forms.ChoiceField(
        label=u'商品种类',
        required=True,
        choices=get_items(),
        widget=forms.RadioSelect())

    # item = forms.RadioChoiceInput(
    #     required=True,
    #     label=u'货物名称',
    #     widget=forms.RadioSelect(
    #         choices=('none','one',)
    #     )
    # )

    num = forms.IntegerField(
        required=True,
        label=u'出库数量',
        widget=forms.TextInput(

        )
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"需要填写更多信息！")
        else:
            cleaned_data = super(OutcomeForm,self).clean()


if __name__ == "__main__":
    get_items()