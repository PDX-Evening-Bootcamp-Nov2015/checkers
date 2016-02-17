from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game, Space, Piece
#@login_required


# Create your views here.
def main(request):
    data = {}
    return render(request, 'checkers_app/home.html', data)

def check_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #authenticate returns a user if this is correct otherwise it returns none
        #if user is none, it means that there was incorrect login info
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("youdidit")
                return HttpResponseRedirect('/getgames/')
        else:
            return HttpResponseRedirect("/register/")

def register(request):
    data = {}
    return render(request, 'checkers_app/register.html', data)

@login_required(login_url='/home/')
def getgames(request):
    data = {}
    return render(request, 'checkers_app/getgames.html', data)

def check_registration(request):
    if request.POST:
        usernamecheck = request.POST['username']
#look in all of the user objects. and find an exact username match that is equal to the variable usernamecheck
        try:
            User.objects.get(username__iexact=usernamecheck)
        except User.DoesNotExist:
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            return HttpResponseRedirect("/home/")
        print("username already created")

def new_game():
    # if request.POST:
    #     black_player_name = request.POST['username']
        black_player_name = "Evan"
        newgame = Game.objects.create(
            black_player = User.objects.get(username__iexact=black_player_name)
        )
        #use these filters to find objects after they have been created
        # red_pieces_list = Piece.objects.filter(color="Red", )
        # black_pieces_list = Piece.objects.filter(color="Black")

        for x in range(8):
            for y in range(8):
                s = Space.objects.create(
                    x_coordinate = x,
                    y_coordinate = y,
                    game_id = newgame,
                )

#
        for x in range(24):
            if x < 12:
                new_red_piece = Piece.objects.create(color="Red")
            elif x >= 12:
                new_black_piece = Piece.objects.create(color="Black")


        spaces = Space.objects.order_by("x_coordinate", "y_coordinate")

        print(spaces)

def board(request):
    data = {}
    print('im being called')
    return render(request, 'checkers_app/checkersBoard.html', data)
