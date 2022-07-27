from django.db import models
from django.db.models import signals
from django.dispatch import receiver  
from django.core.cache import cache

# Create your models here.
class Redirect(models.Model):
    key = models.CharField(max_length=40, blank=False, null=False)
    url = models.TextField()
    active = models.BooleanField(default=True)
    update_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(null=True)

@receiver(signals.post_save, sender=Redirect)
def create_redirec(sender, instance, created, **kwargs) -> None:
    # redirect = Redirect.objects.filter(active=True).values()
    if instance.active:
        cache.set(instance.key, {'url':instance.url}, 30)