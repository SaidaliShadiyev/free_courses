# Generated by Django 5.0.2 on 2024-02-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(to='course.category'),
        ),
    ]
