# Generated by Django 3.2.6 on 2021-08-14 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210814_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='diary_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='main.diary'),
        ),
    ]