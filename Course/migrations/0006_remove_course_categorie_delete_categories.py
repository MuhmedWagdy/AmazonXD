# Generated by Django 4.2 on 2024-01-23 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_categories_remove_course_category_course_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
