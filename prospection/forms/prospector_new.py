#
# IMPORTS
#
# Django
from django import forms


#
# CODE
#
class ProspectorNew(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    is_seller = forms.BooleanField(required=False)

    is_contractor = forms.BooleanField(required=False)

    is_postseller = forms.BooleanField(required=False)
