from django.views import generic
from contactabout.models import AboutProjects


class MainView(generic.TemplateView):
    template_name = "frontpage/main.html"