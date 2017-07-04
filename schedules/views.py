from django.shortcuts import render, redirect
import schedule
import datetime
from schedule.models import Calendar
from schedule.models import Event
from django.contrib.auth.models import User
# from fillials.models import FillialServices 

from django.core.management.base import BaseCommand


# Create your views here.

def create_calendar(request):
    user = request.user
    # user = User.objects.get(user=request.user)
    print(user.first_name)
    cal = Calendar(name="%s" % (user.first_name), slug="%s" % (user.id))
    cal.save()
    print("First calendar is created")
    return redirect("/")


def calendar(request):
    context = {'user': request.user.id}
    print (request.user.id)
    # cal = Calendar.objects.get(slug=user.id)
    return render(request, 'schedules/fullcalendar.html', context)


def create_events(request):
    today = datetime.date.today()
    # services = FillialServices.objects.get(id=id_services)
    cal = Calendar.objects.get(slug=request.user.id)
    data = {
        'title': 'zapis',
        'start': datetime.datetime(today.year, today.month, today.day, 18, 38),
        'end': datetime.datetime(today.year, today.month, today.day, 19, 38),
        'calendar': cal
    }
    event = Event(**data)
    event.save()
    print("Create some events")
    return redirect("/")

def get_events(request, user_id):
        # events = Event.objects.all(slug=user_id)
        return calendar.event_set.all(slug=user_id)
