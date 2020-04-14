# Generated by Django 3.0.4 on 2020-04-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(choices=[('chest', '胸'), ('shoulder', '肩'), ('arm', '腕'), ('leg', '足'), ('back', '背中')], max_length=8)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
