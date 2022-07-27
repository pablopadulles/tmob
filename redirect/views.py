from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Redirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache


@csrf_exempt
def add(request) -> JsonResponse:
    if request.method == 'POST':
        print(request.POST)
        url = request.POST['url']
        key = request.POST['key']
        active = request.POST['active']
        redirect = Redirect(key=key, url=url, active=active, created_at=datetime.now())
        redirect.save()
        return JsonResponse({'status':'ok'})

@csrf_exempt
def update(request, id) -> JsonResponse:
    if request.method == 'POST':
        redirect = Redirect.objects.get(id=id)
        if request.POST.get('url', False):
            redirect.url = request.POST['url']
        if request.POST.get('active', False):
            redirect.active = request.POST['active']
        if request.POST.get('key', False):
            redirect.key = request.POST['key']
        redirect.update_at = datetime.now()
        redirect.save()
        return JsonResponse({'status':'ok'})

@csrf_exempt
def get_redirect(request, key) -> JsonResponse:
    if request.method == 'GET':
        record = cache.get(key)
        if record:
            record['key'] = key
            return JsonResponse(record)
    return JsonResponse({})