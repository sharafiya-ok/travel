# Generated by Django 3.2.16 on 2022-10-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
