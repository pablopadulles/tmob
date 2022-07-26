from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Redirect


def add_redirec(request):
    url = request.POST['url']
    key = request.POST['key']
    active = request.POST['active']
    redirect = Redirect(key=key, url=url, active=active)
    redirect.save()
    return JsonResponse({'status':'ok'})

def update_redirec(request, id):
    redirect = Redirect.objects.get(id=id)
    redirect.url = request.POST['url']
    redirect.key = request.POST['key']
    redirect.active = request.POST['active']
    redirect.save()
    return JsonResponse({'status':'ok'})
