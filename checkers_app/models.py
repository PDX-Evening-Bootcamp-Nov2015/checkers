from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    open_session = models.BooleanField(default=False)
    black_player = models.ForeignKey(User, related_name="black_player")
    red_player = models.ForeignKey(User)
    which_player = models.PositiveSmallIntegerField(default=0)
    jumped = models.BooleanField(default=False)
    turn_over = models.BooleanField(default=False)

class Piece(models.Model):
    king_Status = models.BooleanField(default=False)
    color = models.CharField(max_length=10)

class Space(models.Model):
    x_coordinate = models.PositiveSmallIntegerField(default=0)
    y_coordinate = models.PositiveSmallIntegerField(default=0)
    piece_id = models.BooleanField(default=False)
    black_player = models.ForeignKey(Piece)





