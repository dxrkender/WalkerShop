from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string

from account.models import Client


def send_forgot_message_to_client(email: str) -> bool:
    client = Client.client_manager.get_client_by_email(email=email)

    if not client:
        return False

    try:
        subject = "WalkerShop - Restore password"

        message = render_to_string(
            template_name='account/password_reset.html',
            context={
                'username': client.usename,
                'link': '',
            })



        send_mail(
            subject=subject,
            message="Here is the message.",
            from_email="from@example.com",
            recipient_list=["to@example.com"],
            fail_silently=False,
        )
    except BadHeaderError:
        raise ValueError('Something went wrong while sending the email, please try again.')
    else:
        return True
