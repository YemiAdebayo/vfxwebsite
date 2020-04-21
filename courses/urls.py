from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path

from .views import cg_animation_view, film_making_view, virtual_effect_view

urlpatterns = [
    url(r'^cg-animation/$', cg_animation_view, name="cg-animation"),
    url(r'^film-making/$', film_making_view, name="film-making"),
    url(r'^visual-effects/$', virtual_effect_view, name="visual-effects"),
]
