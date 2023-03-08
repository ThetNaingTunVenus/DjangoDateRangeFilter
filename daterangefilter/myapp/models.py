from django.db import models

# Create your models here.


class Testtable1(models.Model):
    tableid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=225)
    date = models.DateField()
    class Meta:
        db_table = 'test1'