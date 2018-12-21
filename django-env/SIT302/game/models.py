import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


# Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Choice", max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
