# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GreetingsData(models.Model):
    id = models.AutoField(primary_key = True)
    category = models.CharField(max_length=100)
    from_field = models.CharField(max_length=100, db_column='from')  # Field renamed because it was a Python reserved word.
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    id_column = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'greetings_data'

    def __str__(self):
        return self.title