# Generated by Django 4.1.7 on 2023-04-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itikaf', '0013_approval_comment_alter_approval_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='reason',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]