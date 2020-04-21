"""vfxwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.http import HttpResponse
from django.conf.urls.static import static
from pages.views import (home_view, coming_soon_view,
                         about_us_view, team_and_facility_view, students_works_view,
                         xml_sitemap_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('about-us/', about_us_view, name="about-us"),
    path('students-works/', students_works_view, name="students-works"),
    path('team-and-facility/', team_and_facility_view, name="team-and-facility"),
    path('coming-soon/', coming_soon_view, name="coming-soon"),
    path('courses/', include('courses.urls')),
    path('register/', include('registration.urls')),
    url(r'^sitemap.xml/$', xml_sitemap_view, name="sitemap"),
    url(r'^robots.txt', lambda x: HttpResponse(
        "User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
