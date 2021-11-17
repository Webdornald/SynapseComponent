import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    today = datetime.date.today()
    target_day = datetime.date(2031, 11, 7)
    d_day = target_day - today
    complete_day = d_day.days
    return render(request, 'infomationapp/index.html', {'complete_time': complete_day})


def privacypolicy(request):
    return render(request, 'infomationapp/privacy_policy.html')
