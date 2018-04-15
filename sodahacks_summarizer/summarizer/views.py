from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TextForm
from .summarizer import Summarizer


def index(request):
	return render(request, 'summarizer/index.html')

def summarize(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('\nPOST\n')
        # check whether it's valid:
        form = TextForm(request.POST)
        if form.is_valid():
            summ = Summarizer().summary(form.cleaned_data['content'], form.cleaned_data['num_sentences'])
            new_form = TextForm()
            return HttpResponseRedirect('summarizer/index.html', dict(form=new_form, summary=summ))
    else:
        print('\nGET\n')
        form = TextForm()

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'summarizer/index.html', dict(form=form, summary=''))
