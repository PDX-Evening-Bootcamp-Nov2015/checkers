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

def new_game(request):
    if request.POST:
        black_player_name = request.POST['username']
        newgame = Game.objects.create(
        # open_session default value
        # open_session = models.BooleanField(default=False)
        black_player = User.objects.get(username__iexact=black_player_name)
        # red_player = models.ForeignKey(User)
        # which_player = models.PositiveSmallIntegerField(default=0)
        # jumped = models.BooleanField(default=False)
        # turn_over = models.BooleanField(default=False)
        )
        # newgamespace = Space.objects.create(
        for x in range(8):
            for y in range(8):
                s = Space.objects.create(
                x_coordinate = x,
                y_coordinate = y,
                game_id = newgame
                )
        # piece_id = models.ForeignKey(Piece, null=True)
        for x in range(24):
            if x < 12:
                new_red_pieces = Piece.objects.create(
                # king_status = models.BooleanField(default=False)
                color = "Red"
                )
            elif x > 12:
                new_black_pieces = Piece.objects.create(
                # king_status = models.BooleanField(default=False)
                color = "Black"
                )
