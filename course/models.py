from datetime import date

from django.db import models
from user.models import User


class Course(models.Model):

    name = models.CharField(max_length=50, verbose_name="name")
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Paying(models.Model):

    METHOD_CHOICES = [
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_to_pay = models.DateField(default=date.today)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='paying', null=True, blank=True)
    sum = models.PositiveIntegerField()
    method_to_pay = models.CharField(max_length=10, choices=METHOD_CHOICES)
