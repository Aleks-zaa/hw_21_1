# Generated by Django 5.0.6 on 2024-06-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="public",
            field=models.BooleanField(
                blank=True, null=True, verbose_name="признак публикации"
            ),
        ),
    ]
