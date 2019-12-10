from django.shortcuts import render
from django.views.generic import TemplateView

class App1DifferentnameView(TemplateView):
    template_name = 'app1.html'

class App1SamenameView(TemplateView):
    template_name = 'app1_same_file_name.html'