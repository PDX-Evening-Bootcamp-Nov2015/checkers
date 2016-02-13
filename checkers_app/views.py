from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game, Space, Piece
#@login_required


#### Create your views here.
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

### Helper functions here:

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
        # cache modifiers for this loop
        xm, ym = mod[0], mod[1]
        # set and check each new coord
        xn, yn = x + xm, y + ym
        if xn in range(8) and yn in range(8):
            new_coords = (x + xm, y + ym)
            valid_moves.append(new_coords)
    return valid_moves
