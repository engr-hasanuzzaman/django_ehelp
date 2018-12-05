from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  status = models.CharField(max_length=20)
  created_at = models.DateTimeField(default=timezone.now)

  def mark_done(self):
    self.status = 'done'
    self.save()

  def __str__(self):
    return self.title
  