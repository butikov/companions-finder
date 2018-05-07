# Generated by Django 2.0.4 on 2018-05-02 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meet', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_meet', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='meet',
            name='categories',
            field=models.ManyToManyField(related_name='meets', to='category.Category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='meet',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participated_meets', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
    ]