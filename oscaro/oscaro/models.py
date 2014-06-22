from django.db import models


class Var(models.Model):
    """ Custom hash storage in db """

    name = models.CharField(max_length=150)

    value = models.CharField(max_length=150)
