from datetime import datetime
from random import random, randint
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game, Space, Piece

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

def new_game(request):
    # if request.POST:
    #     black_player_name = request.POST['username']
        black_player_name = "Evan3"
        newgame = Game.objects.create(
            black_player = User.objects.get(username__iexact=black_player_name),
        )
        #use these filters to find objects after they have been created
        # red_pieces_list = Piece.objects.filter(color="Red", )
        # black_pieces_list = Piece.objects.filter(color="Black")

        for x in range(8):
            for y in range(8):
                newspace = Space.objects.create(
                    x_coordinate = x,
                    y_coordinate = y,
                    game_id = newgame,
                )

        for x in Space.objects.filter(y_coordinate=0):
            if x.x_coordinate %2 == 0:
                x.piece_id = Piece.objects.create(color="Red", game_id=newgame)

        for x in Space.objects.filter(y_coordinate=2):
            if x.x_coordinate %2 == 0:
                x.piece_id = Piece.objects.create(color="Red", game_id=newgame)

        for x in Space.objects.filter(y_coordinate=1):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Red", game_id=newgame)

        for x in Space.objects.filter(y_coordinate=5):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)

        for x in Space.objects.filter(y_coordinate=6):
            if x.x_coordinate %2 == 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)

        for x in Space.objects.filter(y_coordinate=7):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)

        return HttpResponseRedirect("/game/" + str(newgame.id))

def game(request, game_number):
    current_game = Game.objects.get(id=game_number)
    return render(request, 'checkers_app/checkersBoard.html')

        # spaces = Space.objects.order_by("x_coordinate", "y_coordinate")

def board_click_square(request, variable_square):
    x = variable_square[0]
    y = variable_square[1]
    return JsonResponse({"square":variable_square})

def get_positions(request, game_number2):
    master_list = []
    temp_list = []
    coordinate_dictionary = {}
    current_game2 = game_number2
    for x in Space.objects.all():
        if str(x.game_id.id) == game_number2:
            temp_list.append(x)
    for xx in temp_list:
        print(x.piece_id.id)        
            # temp_list = []
            # temp_list.append(x.x_coordinate)
            # temp_list.append(x.y_coordinate)
            # master_list.append(temp_list)

    return JsonResponse({"key":"yes"})
