from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import User


@receiver(post_save, sender=User)
def post_registration(sender, **kwargs):
    if kwargs['created']:
        send_mail(subject='', message='', from_email='', recipient_list=[], fail_silently=True)
