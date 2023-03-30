# Generated by Django 4.1.7 on 2023-03-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0008_alter_approval_participant_alter_checkin_participant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
