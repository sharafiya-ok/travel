# Generated by Django 3.2.16 on 2022-10-30 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0003_auto_20221029_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc1',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name1',
            new_name='name',
        ),
    ]
