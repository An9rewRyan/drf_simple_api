# Generated by Django 3.2.6 on 2021-08-13 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_diary_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='diary',
        ),
    ]