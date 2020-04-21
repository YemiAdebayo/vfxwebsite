from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from .forms import RegistrationFormForFrontend
from .render import send_email


def register_view(request):
    if request.method == 'POST':
        form = RegistrationFormForFrontend(request.POST)
        if form.is_valid():
            first_name = form.instance.first_name
            last_name = form.instance.last_name
            phone_number = form.instance.phone_number
            email = form.instance.email
            course = form.instance.course
            today = timezone.now()
            params = {
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'email': email,
                'course': course,
                'today': today,
            }

            form.save()
            send_email.delay('registration/pdf.html', params)
            messages.success(
                request, f'Registration successful! You will be contacted by one of our agents within the hour. Thank you!')
            return redirect('register')

    else:
        form = RegistrationFormForFrontend()

    context = {
        'form': form
    }

    return render(request, "registration/register.html", context)
