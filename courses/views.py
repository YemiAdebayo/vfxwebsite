from django.shortcuts import render, redirect

# Create your views here.


def cg_animation_view(request):
    return render(request, "courses/cg-animation.html")
    
def film_making_view(request):
    return render(request, "courses/film-making.html")

def virtual_effect_view(request):
    return render(request, "courses/visual-effect.html")
