from django.db import models


# Helper methods


def get_avatar_path(instance, filename):
    return 'avatars/{}.png'.format(instance.pk)


# Models


class Profile(models.Model):
    firstname = models.CharField(max_length=20, default='')
    lastname = models.CharField(max_length=20, default='')
    hometown = models.CharField(max_length=40, default='')
    description = models.TextField(max_length=500, default='')
    digested_stats = models.OneToOneField('DigestedStats', null=True, related_name='profile')

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class DigestedStats(models.Model):
    games = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    sinks = models.PositiveIntegerField(default=0)

    shots = models.PositiveIntegerField(default=0)
    misses = models.PositiveIntegerField(default=0)
    scorable = models.PositiveIntegerField(default=0)

    throwing_score = models.PositiveSmallIntegerField(default=0)
    catching_score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return 'throwing: {}, catching: {}'.format(self.throwing_score, self.catching_score)


class Game(models.Model):
    date = models.DateField()

    def __str__(self):
        return 'Game on {}'.format(self.date)


class Team(models.Model):
    game = models.ForeignKey('Game', related_name='teams')
    opposing_team = models.OneToOneField('self', null=True)

    def get_combined(self, field='shots'):
        player1, player2 = self.players.all()[0], self.players.all()[1]
        if field == 'points':
            return player1.points + player2.points
        elif field == 'shots':
            return player1.shots + player2.shots
        elif field == 'scorable':
            return player1.scorable + player2.scorable

    def __str__(self):
        return '{} & {}'.format(self.players.all()[0].profile.firstname, self.players.all()[1].profile.lastname)


class Player(models.Model):
    profile = models.ForeignKey('Profile', related_name='players')
    team = models.ForeignKey('Team', related_name='players')
    partner = models.OneToOneField('self', null=True)
    points = models.PositiveIntegerField(default=0)
    shots = models.PositiveIntegerField(default=0)
    misses = models.PositiveIntegerField(default=0)
    scorable = models.PositiveIntegerField(default=0)
    catches = models.PositiveIntegerField(default=0)
    sinks = models.PositiveIntegerField(default=0)

    def get_throwing_score(self):
        return self.scorable / self.shots

    def get_catching_score(self):
        return self.catches / self.team.opposing_team.get_combined('scorable')

    def __str__(self):
        return '{} {} [w/ {}]'.format(self.profile.firstname, self.profile.lastname, self.partner.profile.firstname)
