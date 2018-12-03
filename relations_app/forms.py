"""
A base contact form for allowing users to send email messages through
a web interface.
"""
from django import forms
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.template import loader


class ContactForm(forms.Form):

    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)






##class AkismetContactForm(ContactForm):
##    """
##    Contact form which doesn't add any extra fields, but does add an
##    Akismet spam check to the validation routine.
##    Requires the Python Akismet library, and two configuration
##    parameters: an Akismet API key and the URL the key is associated
##    with. These can be supplied either as the settings AKISMET_API_KEY
##    and AKISMET_BLOG_URL, or the environment variables
##    PYTHON_AKISMET_API_KEY and PYTHON_AKISMET_BLOG_URL.
##    """
##    SPAM_MESSAGE = _(u"Your message was classified as spam.")
##
##    def clean_body(self):
##        if 'body' in self.cleaned_data:
##            from akismet import Akismet
##            akismet_api = Akismet(
##                key=getattr(settings, 'AKISMET_API_KEY', None),
##                blog_url=getattr(settings, 'AKISMET_BLOG_URL', None)
##            )
##            akismet_kwargs = {
##                'user_ip': self.request.META['REMOTE_ADDR'],
##                'user_agent': self.request.META.get('HTTP_USER_AGENT'),
##                'comment_author': self.cleaned_data.get('name'),
##                'comment_author_email': self.cleaned_data.get('email'),
##                'comment_content': self.cleaned_data['body'],
##                'comment_type': 'contact-form',
##            }
##            if akismet_api.comment_check(**akismet_kwargs):
##                raise forms.ValidationError(
##                    self.SPAM_MESSAGE
##                )
##            return self.cleaned_data['body']


class RechercheForm(forms.Form):
    mot = forms.CharField(max_length=100)
 #   message = forms.CharField(widget=forms.Textarea)
 #   envoyeur = forms.EmailField(label="Votre adresse mail")
 #   renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

 
"""class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)"""
class CommentForm(forms.Form):
    commentaires = forms.CharField(max_length=300)
