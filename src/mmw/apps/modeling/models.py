# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.contrib.gis.db import models
from django.forms.models import model_to_dict

from django.contrib.auth.models import User


class District(models.Model):
    state_fips = models.CharField(
        max_length=2,
        help_text='State FIPS codes')
    state_short = models.CharField(
        max_length=2,
        help_text='State or territory name (short)')
    state_long = models.CharField(
        max_length=33,
        help_text='State or territory name (long)')
    district_fips = models.CharField(
        max_length=2,
        help_text='113th congress FIPS codes')
    aff_geoid = models.CharField(
        max_length=13,
        help_text='American FactFinder GeoID')
    geoid = models.CharField(
        max_length=4,
        help_text='GeoID')
    lsad = models.CharField(
        max_length=2,
        help_text='Legal/Statistical Area Description')
    geom = models.MultiPolygonField(
        null=True,
        help_text='District polygon')

    def name(self):
        return str(self.state_short) + ' - ' + str(self.district_fips)

    def __str__(self):
        dictionary = model_to_dict(self)
        dictionary.pop('geom', None)
        return str(dictionary)


class Project(models.Model):
    TR55 = 'tr-55'
    MODEL_PACKAGES = ((TR55, 'Simple Model'),)

    user = models.ForeignKey(User)
    name = models.CharField(
        max_length=255)
    area_of_interest = models.MultiPolygonField(
        help_text='Base geometry for all scenarios of project')
    is_private = models.BooleanField(
        default=True)
    model_package = models.CharField(
        choices=MODEL_PACKAGES,
        max_length=255,
        help_text='Which model pack was chosen for this project')
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True)
    modified_at = models.DateTimeField(
        auto_now=True)

    def __unicode__(self):
        return self.name


class Scenario(models.Model):

    class Meta:
        unique_together = ('name', 'project')

    name = models.CharField(
        max_length=255)
    project = models.ForeignKey(Project, related_name='scenarios')
    is_current_conditions = models.BooleanField(
        default=False,
        help_text='A special type of scenario without modification abilities')
    inputs = models.TextField(
        null=True,
        help_text='Serialized JSON representation of scenario inputs')
    modifications = models.TextField(
        null=True,
        help_text='Serialized JSON representation of scenarios modifications ')
    modification_hash = models.CharField(
        max_length=255,
        null=True,
        help_text='A hash of the values for modifications & inputs to ' +
                  'compare to the existing model results, to determine if ' +
                  'the persisted result apply to the current values')
    results = models.TextField(
        null=True,
        help_text='Serialized JSON representation of the model results')
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True)
    modified_at = models.DateTimeField(
        auto_now=True)

    def __unicode__(self):
        return self.name
