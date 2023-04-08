from django.shortcuts import render
from django.http import HttpResponse

from .models import Activities, Categories, UserActivities

def index(request):
    return render(request, 'Focal_app.html', {'username':'chwah'})


def activity_by_id(request, activityId):
    my_activity = Activities.objects.get(pk=activityId)
    return HttpResponse(f"Activity: {my_activity.name}")

