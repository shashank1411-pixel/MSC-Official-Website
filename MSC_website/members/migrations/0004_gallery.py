# Generated by Django 2.2.2 on 2019-11-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picurl', models.CharField(max_length=300)),
            ],
        ),
    ]