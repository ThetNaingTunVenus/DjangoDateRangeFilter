# Generated by Django 4.1.7 on 2023-03-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_testtable1_delete_testtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtable1',
            name='name',
            field=models.CharField(max_length=225, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testtable1',
            name='tableid',
            field=models.PositiveIntegerField(),
        ),
    ]