# Generated by Django 4.1.7 on 2023-03-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_testtable_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testtable1',
            fields=[
                ('tableid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'test1',
            },
        ),
        migrations.DeleteModel(
            name='Testtable',
        ),
    ]