from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from user.models import User

# Create your views here.

def joinform(request):
    return render(request, 'user/joinform.html')

def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password']) # 퀴리셋(리스트)

    # 로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=false')

    # 로그인 처리
    authuser = result[0]    # 로그인 인증 확인
    request.session['authuser'] = model_to_dict(authuser)      # 로그인 인증이 되었는지 확인 (authuser 있는지 없는지)

    # return HttpResponse('hello world')    # 브라우저에 직접 출력
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')