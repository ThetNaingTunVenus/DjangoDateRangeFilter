# Generated by Django 4.1.7 on 2023-03-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_testtable1_name_alter_testtable1_tableid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtable1',
            name='tableid',
        ),
    ]
