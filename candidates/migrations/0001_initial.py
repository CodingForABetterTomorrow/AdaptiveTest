# Generated by Django 2.0.7 on 2019-02-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testid', models.CharField(max_length=255)),
                ('testpassword', models.CharField(max_length=255)),
                ('studentname', models.CharField(max_length=255)),
                ('studentemail', models.EmailField(max_length=255)),
                ('marks', models.IntegerField(default=-1)),
            ],
        ),
    ]
