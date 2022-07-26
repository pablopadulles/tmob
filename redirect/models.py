from django.db import models

# Create your models here.
class Redirect(models.Model):
    key = models.CharField(max_length=40, blank=False, null=False)
    url = models.TextField()
    active = models.BooleanField(default=True)
    update_at = models.DateTimeField()
    created_at = models.DateTimeField()
