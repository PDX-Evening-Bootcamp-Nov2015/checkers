from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    open_session = models.BooleanField(default=False)
    black_player = models.ForeignKey(User, related_name="black_player")
    red_player = models.ForeignKey(User, null=True)
    which_player = models.PositiveSmallIntegerField(default=0)
    jumped = models.BooleanField(default=False)
    turn_over = models.BooleanField(default=False)


class Piece(models.Model):
    king_status = models.BooleanField(default=False)
    color = models.CharField(max_length=10)
    game_id = models.ForeignKey(Game, null=True)

    def __str__(self):
        return(self.color)

class Space(models.Model):
    x_coordinate = models.PositiveSmallIntegerField(default=0)
    y_coordinate = models.PositiveSmallIntegerField(default=0)
    piece_id = models.ForeignKey(Piece, null=True)
    game_id = models.ForeignKey(Game, null=True)

    def __str__(self):
        return ("x coorindate = " + str(self.x_coordinate) + " y coorindate =" + str(self.y_coordinate) + str(self.piece_id))
