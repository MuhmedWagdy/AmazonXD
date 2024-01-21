# Generated by Django 4.2 on 2024-01-21 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_review', to=settings.AUTH_USER_MODEL),
        ),
    ]