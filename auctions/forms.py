from django import forms
from .models import Listings

class ListForm(forms.ModelForm):

    class Meta:
        model = Listings
        fields = ('title', 'description', 'starting_bid', 'desired_price', 'category', 'image')

