# Generated by Django 3.0.7 on 2021-08-08 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discuss', '0004_auto_20210808_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='chat',
        ),
        migrations.AddField(
            model_name='chat',
            name='chatt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='discuss.stock_model'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='stock_model2',
        ),
    ]
