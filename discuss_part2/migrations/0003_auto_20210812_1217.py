# Generated by Django 3.0.7 on 2021-08-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss_part2', '0002_tutorial_tutorialseries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='tutorial_category',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=200),
        ),
    ]
