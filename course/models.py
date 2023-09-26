from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=50, verbose_name="name")
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
