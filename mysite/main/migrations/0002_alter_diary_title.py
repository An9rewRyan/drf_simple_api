# Generated by Django 3.2.6 on 2021-08-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.TextField(),
        ),
    ]