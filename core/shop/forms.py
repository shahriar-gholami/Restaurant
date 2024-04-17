from django import forms
from .models import Item

class DynamicItemForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DynamicItemForm, self).__init__(*args, **kwargs)
        for item in Item.objects.all():
            self.fields[f'{item.name}'] = forms.IntegerField(label=f'{item.name}')

# مثال استفاده:
# ایجاد یک فرم با 20 فیلد name

