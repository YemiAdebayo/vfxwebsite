from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import os
from celery import shared_task
from django.conf import settings
from random import randint
from django.core.mail import EmailMessage


def render_to_file(path: str, params: dict):
    template = get_template(path)
    html = template.render(params)
    file_name = "{0}-{1}-{2}-ID{3}.pdf".format(
        params['first_name'], params['last_name'], params['today'][:10], randint(1, 1000000))
    file_path = os.path.join(settings.BASE_DIR, "registration_pdf", file_name)
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), pdf)
    return [file_name, file_path]


@shared_task
def send_email(path: str, params: dict):
    get_file_path = render_to_file(path, params)
    email = EmailMessage(
        'New Registration Notification',
        'You have a new registration. Please check the attached file for more detail.',
        settings.DEFAULT_FROM_EMAIL,
        ['info@vfxacademy.com', 'yemi.adebayo.a@gmail.com'])
    email.attach_file(get_file_path[1])
    email.send()
    return [get_file_path[0], get_file_path[1]]
