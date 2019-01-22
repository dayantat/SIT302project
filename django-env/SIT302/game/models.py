import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


# Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")
    EMAIL = "EMAIL"
    review_field = (
        (EMAIL, "Email"),
        ("SPAM", "Spam"),
        ("PHYSICAL", "Physical")
    )
    category_text = models.CharField(max_length=40, choices=review_field, default=EMAIL)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published Recently?"

    def __str__(self):
        return self.question_text


#
# class Category(models.Model):
#     EMAIL = "EMAIL"
#     review_field = (
#         (EMAIL, "Email"),
#         ("SPAM", "Spam"),
#         ("PHYSICAL", "Physical")
#     )
#     category_text = models.CharField(max_length=40, choices=review_field, default=EMAIL)
#
#     question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.category_text


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Choice", max_length=200)
    votes = models.IntegerField(default=0)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
