# Generated by Django 4.1.7 on 2023-03-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0004_alter_applicant_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processing',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='processing',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='processing',
            name='check_out',
        ),
        migrations.AlterField(
            model_name='processing',
            name='additional_info',
            field=models.CharField(max_length=30),
        ),
    ]