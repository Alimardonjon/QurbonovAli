from django.shortcuts import render
from django .views.generic import TemplateView

class Alimardon(TemplateView):
    template_name = 'home.html'
class Fayozbek(TemplateView):
    template_name = 'about.html'