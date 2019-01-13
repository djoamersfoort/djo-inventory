#!/usr/bin/env python3

from django.db import models

"""
class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    token = models.CharField(max_length=32, db_index=True)
    expires = models.DateTimeField()

    def __str__(self):
        return "{0} ({1})".format(self.token, self.user.username)


class Article(models.Model):
    subject = models.CharField(max_length=1024)
    body = models.TextField(max_length=64000)
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return "{0} ({1})".format(self.subject, self.pk)
"""


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, default='')
    photo = models.BinaryField(max_length=2000000, null=True, editable=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.pk)


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField(verbose_name="Url of item specifications / docs")
    properties = models.ManyToManyField(Property)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.pk)
