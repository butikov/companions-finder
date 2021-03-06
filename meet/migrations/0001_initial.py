# Generated by Django 2.0.4 on 2018-05-02 01:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('deleted', models.DateTimeField(editable=False, null=True, verbose_name='Дата удаления')),
                ('text', models.TextField(verbose_name='Текст')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('like_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество лайков')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('meet_time', models.DateTimeField(verbose_name='Время проведения')),
                ('max_participants', models.PositiveIntegerField(default=0, verbose_name='Максимальное кол-во участников')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
