from _future__ import unicode_literals

from django.db import models

#Define a Django model to represent the settings for the light control
class Setting(models.Model):
    auto_mode = models.BooleanField(default=false)
    led_state = models.BooleanField(default=false)