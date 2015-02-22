from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Essay(models.Model):
    user = models.ForeignKey(User)
    title = models.TextField()
    url = models.TextField()
    markdown = models.TextField()
    last_update = models.DateTimeField()
    def __unicode__(self):
        return self.title + " (" + self.user.username + ")"