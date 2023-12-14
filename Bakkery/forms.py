from django import forms

class ImageSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
