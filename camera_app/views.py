from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == 'admin' and password == '':
        return render(request, 'cameras.html')
    else:
        responseData = {
            'status': 'Fail to login'
        }
    return JsonResponse(responseData)

