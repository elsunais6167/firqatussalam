# Generated by Django 4.1.7 on 2023-03-26 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('next_of_kin_name', models.CharField(max_length=100)),
                ('next_of_kin_phone', models.CharField(max_length=20)),
                ('medical_condition', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('id_card_no', models.CharField(max_length=20)),
                ('id_image', models.ImageField(upload_to='')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mosque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=300)),
                ('accepting_applications', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itikaf.lga')),
            ],
        ),
        migrations.CreateModel(
            name='MosqueAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mosque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itikaf.mosque')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('check_in', models.DateField(blank=True)),
                ('check_out', models.DateField(blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='itikaf.mosqueadmin')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='itikaf.applicant')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='itikaf.mosqueadmin'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='mosque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itikaf.mosque'),
        ),
    ]