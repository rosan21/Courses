# Generated by Django 4.0.5 on 2022-06-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('resources', models.FileField(upload_to='files/resource')),
                ('length', models.IntegerField()),
            ],
        ),
    ]
