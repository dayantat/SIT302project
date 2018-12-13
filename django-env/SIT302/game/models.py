from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return "List: {}".format(self.question)


class Choice(models.Model):
    question = models.ForeignKey("Question", related_name="choices", on_delete=models.CASCADE)
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

    def __str__(self):
        return "Choice {}".format(self.choice)