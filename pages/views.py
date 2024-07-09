from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class MainPageView(TemplateView):
    template_name = 'main.html'