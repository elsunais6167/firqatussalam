# Generated by Django 4.1.7 on 2023-04-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0016_alter_comment_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='action',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='additional_info',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
