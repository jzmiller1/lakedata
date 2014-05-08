from django.views import generic
from contactabout.models import AboutProjects, ContactInfo, ContactForm
from django.core.urlresolvers import reverse_lazy


class AboutDetail(generic.DetailView):
    model = AboutProjects
    template_name = 'contactabout/about_detail.html'
    context_object_name = 'project'


class ContactFormView(generic.CreateView):
    model = ContactInfo
    template_name = 'contactabout/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactabout:confirmation')


class ContactConfirmation(generic.TemplateView):
    template_name = 'contactabout/ContactThanks.html'