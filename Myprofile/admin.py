from django.contrib import admin

from .models import workexp, education, skills

admin.site.register(workexp)
admin.site.register(education)
admin.site.register(skills)