from django.db import models
from django.conf import settings
from django.utils import timezone
from model_utils import Choices

# Create your models here.
class Ticket(models.Model):
  STATUSES = Choices(
        (0, 'open', 'Open'),
        (1, 'reviewed', 'Reviewed by Manager'),
        (2, 'closed', 'Closed'),
      )

  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  status = models.IntegerField(default=STATUSES.open, choices=STATUSES)
  created_at = models.DateTimeField(default=timezone.now)

  def mark_done(self):
    self.status = 'done'
    self.save()

  def __str__(self):
    return self.title
  