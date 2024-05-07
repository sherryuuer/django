from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link


class LinkListView(ListView):
    # Link.object.all()
    # context = { 'link': links }
    # return render(request, 'link_plant/link_list.html', context)
    model = Link
    # template must be model_list.html --> link_list.html


class LinkCreateView(CreateView):
    # create form.py
    # check if it is a post
    # return empty form or save the data
    model = Link
    # template - model_form.html
    # figure out what fields - could pass a list
    fields = "__all__"
    # success_url
    success_url = reverse_lazy('link-list')


class LinkUpdateView(UpdateView):
    # Shares same template as create view
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy('link-list')


class LinkDeleteView(DeleteView):
    # send a form with a single 'confirm delete btn'
    # template - model_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')


# external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)
