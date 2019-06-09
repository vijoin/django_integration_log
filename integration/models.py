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

class IntegrationLines(models.Model):
    """Integration Details"""

    module_id = models.CharField(max_length=100)  #m2o hacia integration.module
    repository_id = models.CharField(max_length=100)  #m2o hacia integration.repository
    server_id = models.CharField(max_length=100)  #m2o hacia integration.server
    db_id = models.CharField(max_length=100)  #m2o hacia integration.server.bd
    description = models.TextField(max_length=100)
    state = models.CharField(max_length=100,
                             choices=[('draft', 'Draft'),
                                      ('testing', 'Testing'),
                                      ('confirmed', 'Confirmed'),
                                      ('production', 'Production')])
    validator_ids = models.CharField(max_length=100)  #m2m to users

    def __str__(self):
        return "{} - {}".format(self.module_id, self.state)
