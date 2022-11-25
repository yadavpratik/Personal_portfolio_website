from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    user=request.user
    print(user)
    print(user.id)

    user.id=6

    profile=userprofile.objects.get(connection=user.id)
    educations=education.objects.filter(connection=user.id)
    experiences=experience.objects.filter(connection=user.id)
    skillss=skills.objects.filter(connection=user.id)
    project=projects.objects.filter(connection=user.id)
    service=services.objects.filter(connection=user.id)
    portfollio=portfollios.objects.filter(connection=user.id)
    intros=intro.objects.get(connection=user.id)

    print(skillss)

    print(profile)
    context={'profile':profile,
            'educations':educations,
            'experiences':experiences,
            'skills':skillss,
            'service':service,
            'portfollio':portfollio,
            'intro':intros,
            'project':project

            }

    return render(request,'index.html',context)



