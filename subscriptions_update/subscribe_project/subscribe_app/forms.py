from django.forms import ModelForm
from subscribe_app.models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email']