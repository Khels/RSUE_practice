# Generated by Django 3.2.4 on 2021-06-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0002_auto_20210622_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduate',
            name='cafedra',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Кафедра'),
        ),
    ]
