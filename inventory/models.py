#!/usr/bin/env python3

from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, default='')
    photo = models.BinaryField(max_length=4000000, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.pk)


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.BinaryField(max_length=20000000)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    url = models.URLField(verbose_name="Url of item specifications / docs")
    properties = models.ManyToManyField(Property)
    document = models.ForeignKey(Document, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.pk)
