from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    class Meta:
        abstract = True
