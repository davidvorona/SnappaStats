from django.db import models


class Profile(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class Game(models.Model):
    date = models.DateField()


class Team(models.Model):
    opposing_team = models.OneToOneField('self')
    game = models.ForeignKey('Game', related_name='teams')

    def get_combined(self, field='shots'):
        player1, player2 = self.players[0], self.players[1]
        if field == 'points':
            return player1.points + player2.points
        elif field == 'shots':
            return player1.shots + player2.shots
        elif field == 'scorable':
            return player1.scorable + player2.scorable


class Player(models.Model):
    profile = models.ForeignKey('Profile', related_name='players')
    team = models.ForeignKey('Team', related_name='players')
    points = models.PositiveIntegerField(default=0)
    shots = models.PositiveIntegerField(default=0)
    misses = models.PositiveIntegerField(default=0)
    scorable = models.PositiveIntegerField('scorable shots', default=0)
    catches = models.PositiveIntegerField(default=0)
    sinks = models.PositiveIntegerField(default=0)

    def get_throwing_score(self):
        return self.scorable / self.shots

    def get_catching_score(self):
        return self.catches / self.team.opposing_team.get_combined('scorable')


def generate_game(data):
    """
    :param data: Data that represents game to be generated.
    {
        date,
        teams: [
            {
                players: [
                    {
                        firstname, lastname, points, shots, misses, scorable, catches, sinks
                    }, {
                    ...
                    }
                ]
            }, {
                players: [
                    {
                        ...
                    }, {
                        ...
                    }
                ]
            }
        ]
    }
    :return:
    """
    game = Game()
    game.date = data['date']
    for team_data in data['teams']:
        team = Team()
        for player_data in team_data['players']:
            player = Player()
            player.profile = Profile.objects.get(firstname=player_data['firstname'], lastname=player_data['lastname'])
            player.points = player_data['points']
            player.shots = player_data['shots']
            player.misses = player_data['misses']
            player.scorable = player_data['scorable']
            player.catches = player_data['catches']
            player.sinks = player_data['sinks']
            player.team = team
            player.save()
        team.game = game
        team.save()
    game.save()
