from django.conf import settings
from django.db import models

# Create your models here.

from .validators import validate_content

class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return "/tweet/%i/" % self.id

    # def clean(self, *args, **kwargs):
    #   content = self.content
    #   if content == "abc":
    #       raise ValidationError("Content Cannot be ABC")
    #   return super(Tweet, self).clean(*args, **kwargs)