# Generated by Django 4.2.7 on 2023-12-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='roles',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'admin'), (2, 'employee')], null=True),
        ),
    ]
