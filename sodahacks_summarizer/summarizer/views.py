from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def index(request):
	return render(request, 'summarizer/index.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})