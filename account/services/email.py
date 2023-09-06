from django.core.mail import send_mail, BadHeaderError

from account.models import Client


def send_forgot_message_to_client(email: str) -> bool:
    client = Client.client_manager.get_client_by_email(email=email)

    if not client:
        return False


    try:
        send_mail(
            subject="Subject here",
            message="Here is the message.",
            from_email="from@example.com",
            recipient_list=["to@example.com"],
            fail_silently=False,
        )
    except BadHeaderError:
        raise ValueError('Something went wrong while sending the email, please try again.')
    else:
        return True
