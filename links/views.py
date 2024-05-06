import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Link
from .forms import LinkForm


def index(request):
    links = Link.objects.all()
    context = {'links': links}
    return render(request, 'links/index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()

    return redirect(link.url)


def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid:
            # save the data and return to homepage
            form.save()
            return redirect(reverse('link-home'))
    else:
        form = LinkForm()
    context = {'form': form}
    return render(request, 'links/add.html', context)
