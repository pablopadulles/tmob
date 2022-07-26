from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Redirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    if request.method == 'POST':
        print(request.POST)
        url = request.POST['url']
        key = request.POST['key']
        active = request.POST['active']
        redirect = Redirect(key=key, url=url, active=active, created_at=datetime.now())
        redirect.save()
        return JsonResponse({'status':'ok'})

@csrf_exempt
def update(request, id):
    if request.method == 'POST':
        redirect = Redirect.objects.get(id=id)
        redirect.url = request.POST['url']
        redirect.key = request.POST['key']
        redirect.active = request.POST['active']
        redirect.update_at = datetime.now()
        redirect.save()
        return JsonResponse({'status':'ok'})
