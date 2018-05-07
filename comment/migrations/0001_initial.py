# Generated by Django 2.0.4 on 2018-05-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('deleted', models.DateTimeField(editable=False, null=True, verbose_name='Дата удаления')),
                ('text', models.TextField(verbose_name='Текст')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('like_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество лайков')),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]