from django.contrib.auth.models import AbstractUser
from django.db import models
from game.models import Choice

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    # Cannot get this to work, cannot pull score from game model
    # point = models.IntegerField(Choice.points, default=0)
    #
    # def save(self, *args, **kwargs):
    #     self.score = self.total_score()
    #     super(Profile, self).save(*args, **kwargs)
    #
    # def total_score(self):
    #     try:
    #         value_a = self.score
    #         value_b = self.point
    #         return value_a + value_b
    #     except KeyError:
    #         return 0

    def __str__(self):
        return self.user.username
