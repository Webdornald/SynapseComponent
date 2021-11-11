from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'infomationapp/index.html')


def privacypolicy(request):
    return render(request, 'infomationapp/privacy_policy.html')
