# Generated by Django 4.1.7 on 2024-01-01 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mood", "0002_alter_mooddata_moodtype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mooddata",
            name="dateposted",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]