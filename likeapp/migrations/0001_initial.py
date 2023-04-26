# Generated by Django 4.2 on 2023-04-26 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0003_article_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='articleapp.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'article')},
            },
        ),
    ]
