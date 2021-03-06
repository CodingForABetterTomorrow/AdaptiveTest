# Generated by Django 2.1.7 on 2019-02-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20180823_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=255)),
                ('optionA', models.CharField(max_length=100)),
                ('optionB', models.CharField(max_length=100)),
                ('optionC', models.CharField(max_length=100)),
                ('optionD', models.CharField(max_length=100)),
                ('rightAns', models.CharField(max_length=1)),
                ('diff', models.CharField(max_length=10)),
                ('field', models.CharField(max_length=10)),
                ('origin', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestID', models.CharField(max_length=10)),
                ('passwd', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('Company', models.CharField(max_length=40)),
                ('math', models.IntegerField(default=0)),
                ('lr', models.IntegerField(default=0)),
                ('eng', models.IntegerField(default=0)),
            ],
        ),
    ]
