# Generated by Django 4.1.7 on 2023-04-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0012_stateadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='comment',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='approval',
            name='approved',
            field=models.CharField(max_length=30),
        ),
    ]
