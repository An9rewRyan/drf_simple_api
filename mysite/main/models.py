from django.db import models
from random import randint
from hashids import Hashids
import uuid

def make_token():

    hashids = Hashids(salt=uuid.uuid4().hex, min_length=7)
    hash = hashids.encode(randint(1,100000000000))

    return hash
# Create your models here.
class Diary(models.Model):
    title = models.TextField()
    expiration = models.DateTimeField(default='2100-09-25 23:19')
    is_private = models.BooleanField(default=False)


    token = models.CharField(max_length=10, default=make_token())


class Note(models.Model):
    text = models.CharField(max_length=1000000)
    diary = models.CharField(max_length=10, default='')
