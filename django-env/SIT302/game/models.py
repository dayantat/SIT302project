from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey("Question", related_name="choices")
    choice = models.CharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # No Duplicated Choice per question
            ("question", "choice"),
            # No Duplicated position per question
            ("question", "position")
        ]
        ordering = ("position",)