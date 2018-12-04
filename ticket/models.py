from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  title = models.CharField(max=50)
  description = models.CharField(max=200, min=10)
  status = models.CharField()
  created_at = models.DateTimeField(default=timezone.now)

  def mark_done(self):
    self.status = 'done'
    self.save()

  def __str__(self):
    return self.title
  