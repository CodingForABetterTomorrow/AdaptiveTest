# Generated by Django 2.1.7 on 2019-02-19 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_questions_tests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Tests',
            new_name='Test',
        ),
    ]
