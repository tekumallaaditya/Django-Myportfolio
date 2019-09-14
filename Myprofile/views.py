from django.shortcuts import render

from .models import workexp, education

def profile(request):
    work_details = workexp.objects
    edu_details = education.objects
    context = {'work': work_details, 'edu_details': edu_details}
    return render(request, 'Myprofile/profile.html', context)
