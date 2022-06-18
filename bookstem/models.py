

from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    desc= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    notes = models.TextField()
    book = models.ManyToManyField(Books, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




