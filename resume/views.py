from django.shortcuts import render

from .models import showresume

def resume(request):
    resume = showresume.objects.all()
    context = {'resume': resume}
    return render(request, 'resume/resume.html', context )
