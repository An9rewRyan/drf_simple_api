from django.core.exceptions import DisallowedRedirect
from django.db import models
from random import randint
from hashids import Hashids
import uuid

# Create your models here.
class Diary(models.Model):
    title = models.TextField()
    expiration = models.DateTimeField(default='2100-09-25 23:19')
    is_private = models.BooleanField(default=False)
    
class Note(models.Model):
    diary_id = models.ForeignKey(Diary, related_name='notes', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000000)
    
    def __str__(self):
        return '{}: {}'.format(self.pk, self.text)
