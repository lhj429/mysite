from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board

# Create your views here.

def index(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}

    return render(request, 'board/list.html', context)

def writeform(request):
    # 인증 체크 (보안)
    try:
        if request.session['authuser'] is not None:
            return render(request, 'board/write.html')
    except:
        return HttpResponseRedirect('/user/loginform')

def write(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = request.session['authuser']['id']
    board.save()

    return HttpResponseRedirect('/board')

def viewform(request):
    if (request.GET['mdf'] is None):
        board = Board.objects.filter(id=request.GET['id']).get()
        board.hit += 1
        board.save()

    board = Board.objects.filter(id=request.GET['id']).values()
    data = {'board': board}

    return render(request, 'board/view.html', data)

    # try:
    #     if request.session['authuser'] is not None:
    #         if(request.GET['mdf']==1):
    #             board = Board.objects.filter(id=request.GET['id']).get()
    #             board.hit += 1
    #             board.save()
    #
    #         board = Board.objects.filter(id=request.GET['id']).values()
    #         data = {'board': board}
    #
    #     return render(request, 'board/view.html', data)
    # except:
    #     return HttpResponseRedirect('/user/loginform')

def delete(request):
    try:
        if request.session['authuser'] is not None:
            Board.objects.filter(user=request.session['authuser']['id']).filter(id=request.GET['id']).delete()

            return HttpResponseRedirect('/board')
    except:
        return HttpResponseRedirect('/user/loginform')

def modifyform(request):
    board = Board.objects.filter(id=request.GET['id']).values()
    data = {'board':board}

    return render(request, 'board/modify.html', data)

def modify(request):
    board = Board.objects.filter(id=request.GET['id']).get()
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board/viewform?id=' + request.GET['id'] + '&mdf=true')

def search(request):
    board_list = Board.objects.filter(title=request.POST['kwd']).all()
    context = {'board_list': board_list}

    return render(request, 'board/list.html', context)