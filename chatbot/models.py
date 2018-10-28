from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    def __unicode__(self):
        return self.tag


class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    def __unicode__(self):
        return self.location


class Service(models.Model):
    name = models.CharField(max_length=30)
    minAge = models.IntegerField()
    maxAge = models.IntegerField()
    location = models.ManyToManyField(Location)
    gender = models.CharField(max_length=10, blank=True, default='')
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=140)
    link = models.CharField(max_length=140)
