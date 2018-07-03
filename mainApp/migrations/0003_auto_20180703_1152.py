# Generated by Django 2.0.6 on 2018-07-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180702_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='refresh_token_token',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authtoken',
            name='token',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]