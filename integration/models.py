from django.db import models


class Integration(models.Model):
    """ Main model to register all integrations """

    sequence = models.CharField(max_length=10)
    date = models.DateTimeField()
    user_id = models.CharField(max_length=100)
    line_ids = models.CharField(max_length=100)

    def __str__(self):
        return "[{}] - @{} - {}".format(self.sequence,
                                        self.user_id,
                                        self.date,
                                        )