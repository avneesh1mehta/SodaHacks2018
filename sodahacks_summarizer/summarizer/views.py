from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TextForm
from .summarizer import Summarizer

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            summ = Summarizer().summary(form.cleaned_data['content'], form.cleaned_data['num_sentences'])
            new_form = TextForm()
            return render(request, 'summarizer/index.html', dict(form=new_form, summary=summ))

    return render(request, 'summarizer/index.html', dict(form=TextForm(), summary=""))
