# Generated by Django 4.0.3 on 2022-06-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Basic', max_length=100)),
                ('thumbnail_sizes', models.CharField(default='200', max_length=200)),
                ('link_to_original', models.IntegerField(default=0)),
                ('expiring', models.CharField(default='0', max_length=20)),
            ],
        ),
    ]
