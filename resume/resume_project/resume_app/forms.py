from django.forms import ModelForm
from .models import Subscribe, Post


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['first_name', 'last_name', 'email']