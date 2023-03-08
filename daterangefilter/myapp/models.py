from django.db import models

# Create your models here.


class Testtable1(models.Model):

    name = models.CharField(primary_key=True,max_length=225)
    date = models.DateField()
    class Meta:
        db_table = 'test1'