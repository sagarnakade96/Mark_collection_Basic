# Generated by Django 3.2.9 on 2021-11-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('usn', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=100)),
                ('lname', models.CharField(default='', max_length=100)),
                ('ten_ma', models.CharField(default='', max_length=100)),
                ('tw_ma', models.CharField(default='', max_length=100)),
            ],
        ),
    ]