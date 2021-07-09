from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Message(models.Model):
    transitioning = models.BooleanField(default=False)
