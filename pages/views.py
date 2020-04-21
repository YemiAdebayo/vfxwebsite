from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib import auth
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import CustomerInquiryForm


def home_view(request):
    if request.method == 'POST':
        form = CustomerInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Message sent! You will receive response by email shortly. Thank you!')
            return redirect('home')

    else:
        form = CustomerInquiryForm
    context = {
        'form': form
    }

    return render(request, "pages/index.html", context)


def coming_soon_view(request):
    return render(request, "pages/base.html")


def about_us_view(request):
    return render(request, "pages/about.html")


def team_and_facility_view(request):
    return render(request, "pages/team-and-facility.html")


def students_works_view(request):
    return render(request, "pages/students-works.html")


def xml_sitemap_view(request):
    return render(request, "pages/sitemap.xml")
