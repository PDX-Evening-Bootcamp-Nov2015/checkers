from datetime import datetime
from random import random, randint
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game, Space, Piece

#### Create your views here.
def main(request):
    data = {}
    return render(request, 'checkers_app/home.html', data)

def game(request):
    context = {}
    return render(request, 'checkers_app/game.html', context)

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
                x.save()


        for x in Space.objects.filter(y_coordinate=2):
            if x.x_coordinate %2 == 0:
                x.piece_id = Piece.objects.create(color="Red", game_id=newgame)
                x.save()

        for x in Space.objects.filter(y_coordinate=1):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Red", game_id=newgame)
                x.save()

        for x in Space.objects.filter(y_coordinate=5):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)
                x.save()

        for x in Space.objects.filter(y_coordinate=6):
            if x.x_coordinate %2 == 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)
                x.save()

        for x in Space.objects.filter(y_coordinate=7):
            if x.x_coordinate %2 != 0:
                x.piece_id = Piece.objects.create(color="Black", game_id=newgame)
                x.save()

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
    for x in Space.objects.all():
        if str(x.game_id.id) == game_number2:
            print(x.piece_id)

    #         temp_list.append(x)
    # for xx in temp_list:
    #     print(x.piece_id.id)
                # temp_list = []
                # temp_list.append(x.x_coordinate)
                # temp_list.append(x.y_coordinate)
                # master_list.append(temp_list)

    return JsonResponse({"key":master_list})

def board(request):
    data = {}
    print('im being called')
    return render(request, 'checkers_app/checkersBoard.html', data)

### Helper functions here:

def check_space(coords, game_id):
    '''
    queries for the peice ID in a specific set of coords in a specific game
    '''
    # coords must be a tuple or list in x, y format
    return Space.objects.filter(x_coordinate=coords[0],y_coordinate=coords[1],game_id=game_id)

def is_king(piece_id):
    '''
    checks if a corresponding peice ID is kinged
    for use in move validation views
    '''
    return Piece.objects.get(pk=piece_id).king_status

def gen_move_coords(coords):
    '''
    generates a list of up to four valid moves (not jumps)
    based on a set of coordinates
    '''
    # coords as tuple (x, y)
    valid_moves = []
    x, y = coords[0], coords[1]
    # modifiers below define the relation to four possible valid moves
    modifiers = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
    # apply each modifier to original coordinates
    for mod in modifiers:
        # set and check each new coord
        xn, yn = x + mod[0], y + mod[1]
        if xn in range(8) and yn in range(8):
            valid_moves.append((xn, yn))
    return valid_moves

def gen_jump_coords(coords):
    '''
    generates a list of up to four valid jumps (not moves)
    based on a set of coordinates
    '''
    # coords as tuple (x, y)
    valid_jumps = []
    x, y = coords[0], coords[1]
    # modifiers below define the relation to four possible valid moves
    modifiers = [(-2, 2), (2, -2), (-2, -2), (2, 2)]
    # apply each modifier to original coordinates
    for mod in modifiers:
        # set and check each new coord
        xn, yn = x + mod[0], y + mod[1]
        if xn in range(8) and yn in range(8):
            new_coords = (xn, yn)
            valid_jumps.append(new_coords)
    return valid_jumps


def check_jump_valid(start_coords, end_coords):
    '''
    takes the start and end coordinates of a possible jump
    and determines if there is an opposing player piece in between
    returns boolean indicating if the jump is valid
    '''
    # calculate coordinates of intervening space
    intervene_x = (start_coords[0] + end_coords[0]) / 2
    intervene_y = (start_coords[1] + end_coords[1]) / 2
    intervening = (intervene_x, intervene_y)
