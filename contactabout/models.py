from django.db import models
from django import forms


class AboutProjects(models.Model):
    name = models.CharField(max_length=100)
    about_us = models.CharField(max_length=500)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.project_name


class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name + ":  " + self.subject


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('name', 'email', 'subject', 'message')