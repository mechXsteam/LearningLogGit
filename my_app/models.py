from django.db import models
from django.contrib.auth.models import User

# Create your models here.


"Defining Topic Model"
class Topics(models.Model):
    """A topic that a user is learning about"""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


"Defining Entry Model"
class Entry(models.Model):
    """Something specefic learned about a topic"""
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."





