# Generated by Django 4.2 on 2023-04-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0003_article_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="article", name="dislike", field=models.IntegerField(default=0),
        ),
    ]