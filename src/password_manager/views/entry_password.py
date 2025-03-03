
from django.shortcuts import render
from password_manager.models import EntryPassword
from password_manager.forms import EntryPasswordForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from core.base.mixins import MixinFormValidTemplate

class HomeView(ListView):
    template_name = "home.html"
    model = EntryPassword
    context_object_name = "websites"


class WebSiteDataDetailView(DetailView):
    template_name = "website_data_detail.html"
    model = EntryPassword
    context_object_name = 'website'


class WebSiteDataCreateView(MixinFormValidTemplate, CreateView):
    template_name = "website_form_create.html"
    model = EntryPassword
    form_class = EntryPasswordForm
    context_object_name = "website"
    success_url = '/'
    success_template = "website_data_detail.html"


    
    
class WebSiteDataUpdateView(MixinFormValidTemplate, UpdateView):
    template_name = "website_form_update.html"
    model = EntryPassword
    form_class = EntryPasswordForm
    context_object_name = 'website'
    success_url = '/'
    success_template = "website_data_detail.html"
    

class WebSiteDataDeleteView(DeleteView):
    model = EntryPassword
    success_url = '/'