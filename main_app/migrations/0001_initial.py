# Generated by Django 4.1.1 on 2022-10-01 22:30

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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='activity date')),
                ('activity', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('coatcolor', models.CharField(max_length=15)),
                ('notes', models.TextField(max_length=250)),
                ('ownername', models.CharField(max_length=20)),
                ('ownerphone', models.CharField(max_length=12)),
                ('owneraddress', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DogPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dog')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.activity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dog'),
        ),
    ]
