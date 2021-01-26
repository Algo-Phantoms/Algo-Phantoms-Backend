import threading
import smtplib
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from AlgoPhantomBackend.local_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send(fail_silently = False)
    
    
def send_mail(request, name, link_user, to_email):
    current_site = get_current_site(request)
    email_subject = 'Verify Your Email Address'
    message = render_to_string('core/account_active_email.html', {
        'name': name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(link_user.id)),
        'token': account_activation_token.make_token(link_user),
    })
    email = EmailMessage(
        email_subject, message, to=[to_email]
    )
    EmailThread(email).start()
    return True

