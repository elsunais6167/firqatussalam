# Generated by Django 4.1.7 on 2023-03-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0003_alter_applicant_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
