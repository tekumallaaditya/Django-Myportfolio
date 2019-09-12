from django.shortcuts import render
from .models import introPageInfo


def welcome(request):
    intro_info = introPageInfo.objects.all()
    # context = {
    #     'first_info': intro_info.first_intro,
    #     'main_into': intro_info.main_into,
    #     'main_pic': intro_info.main_pic
    # }
    context = {
        'intro': intro_info
    }
    return render(request, 'home/home.html', context)
