# Generated by Django 3.0.5 on 2020-05-24 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='doctor',
        ),
    ]
