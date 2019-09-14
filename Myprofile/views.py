from django.shortcuts import render

from .models import workexp, education, skills

def profile(request):
    work_details = workexp.objects
    edu_details = education.objects
    skill_set = skills.objects
    context = {'work': work_details, 'edu_details': edu_details, 'skills': skill_set}
    return render(request, 'Myprofile/profile.html', context)
