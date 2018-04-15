from django import forms

class TextForm(forms.Form):
    num_sentences = forms.IntegerField()
    content = forms.CharField(widget=forms.Textarea)
