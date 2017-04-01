from __future__ import unicode_literals

from django.db import models

class Word(models.Model):
    word_eng = models.CharField(max_length = 200)
    word_pol = models.CharField(max_length = 200)
    word_level = models.IntegerField(default = 0)
