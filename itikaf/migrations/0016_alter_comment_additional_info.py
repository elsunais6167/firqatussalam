# Generated by Django 4.1.7 on 2023-04-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0015_comment_action_alter_comment_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='additional_info',
            field=models.CharField(max_length=500, null=True),
        ),
    ]