# Generated by Django 3.1.5 on 2021-02-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
    ]