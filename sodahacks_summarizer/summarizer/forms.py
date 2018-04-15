from django import forms

class TextForm(forms.Form):
    num_sentences = forms.IntegerField(label="Num Sent")
    content = forms.CharField(label="Content", widget=forms.Textarea)
