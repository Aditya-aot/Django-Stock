# Generated by Django 3.0.7 on 2021-08-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss_part2', '0003_auto_20210812_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialcategory',
            name='category_slug',
        ),
        migrations.RemoveField(
            model_name='tutorialcategory',
            name='category_summary',
        ),
    ]