import logging

import simplejson
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render

from .models import User


# Create your views here.

def reg(request: HttpRequest):
    try:
        # payload = json.loads(request.body.decode())
        payload = simplejson.loads(request.body)
        email = payload['email']
        # 数据库中查看Email有没有
        qs = User.objects.filter(email=email)
        print(qs.query, '---------------')
        if qs:  # email已经存在了
            return HttpResponseBadRequest()
        name = payload['name']
        password = payload['password']
        print(email, name, password)
        logging.info(email)
        user = User()
        user.email = email
        user.password = password
        user.name = name

        try:
            user.save()
            return JsonResponse({'user_id': user.id})
        except Exception as e:
            raise
    except Exception as e:
        logging.info(e)
    return HttpResponseBadRequest()


def index(request: HttpRequest):
    return render(request, 'index.html')
