from random import randint
from django.core.mail import send_mail
from django.conf import settings


def SubscriptionView(email_address):
    number = randint(10000, 99999)
    send_mail('Код потверждения', '%s' % str(number),
              settings.EMAIL_HOST_USER, ['%s' % email_address],
              fail_silently=False)
    return number
