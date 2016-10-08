from django.shortcuts import render

from .forms import FormExample


def home(request):
    form = FormExample()
    context = {"form": form}
    return render(request, 'index.html', context)
