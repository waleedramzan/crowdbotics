from django.db import models
from jsonfield import JSONField


class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Types(models.Model):
    animal_type = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.animal_type


class Animal(models.Model):
    name = JSONField(blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    type = models.ForeignKey('Types', related_name='type_of_animal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    animal_id = models.ForeignKey('Animal', related_name='owner_animals', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

