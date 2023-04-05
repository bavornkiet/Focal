from django.shortcuts import render
from django.http import HttpResponse

from .models import Activities, Categories, UserActivities

def index(request):
    return HttpResponse("Hello world")


def activity_by_id(request, id):
    my_activity = Activities.objects.get(pk='activityId')
    return HttpResponse(f"Activity: {my_activity.name}")

