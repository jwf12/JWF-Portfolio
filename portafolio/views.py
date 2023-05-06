from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import generic

# Create your views here.
class ListProjects(generic.TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get('https://jwf3.pythonanywhere.com')
        project = response.json()
        context['projects']= project
        return context