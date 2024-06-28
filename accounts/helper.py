from django.core.mail import send_mail
from django.conf import settings


def send_verify_mail(email, token):
    subject = 'Do Not Reply: You have a new message!'
    message = f'Hi, thank you for registering in BlogFame. Please click on this link to verify your email address: https://blogfame.herokuapp.com/verify/{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def forgot_password_mail(email, token):
    subject = 'Do Not Reply: You have a new message!'
    message = f'Hi, It seems you forgot your password. Please click on this link to change your password: https://blogfame.herokuapp.com/Change_password/{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)