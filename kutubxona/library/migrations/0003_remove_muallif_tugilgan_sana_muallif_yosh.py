# Generated by Django 4.1.5 on 2023-01-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_admin_kitob_talaba_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muallif',
            name='tugilgan_sana',
        ),
        migrations.AddField(
            model_name='muallif',
            name='yosh',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
