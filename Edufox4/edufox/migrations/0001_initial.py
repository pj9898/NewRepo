# Generated by Django 2.0.6 on 2018-09-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
                ('YourName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]