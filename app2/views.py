from django.shortcuts import render
from django.views.generic import TemplateView

class App2DifferentnameView(TemplateView):
    template_name='app2.html'

class App2SamenameView(TemplateView):
    template_name = 'app2_same_file_name.html'