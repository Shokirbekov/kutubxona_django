# Generated by Django 4.1.5 on 2023-01-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tirik', models.BooleanField(default=True)),
                ('kitob_soni', models.PositiveSmallIntegerField()),
                ('tugilgan_sana', models.DateField()),
            ],
        ),
    ]
