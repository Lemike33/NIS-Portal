from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import Post


@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.title} {instance.text}'
    else:
        subject = f'Appointment changed for {instance.title} {instance.text}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )


