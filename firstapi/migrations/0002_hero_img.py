# Generated by Django 3.1.1 on 2020-10-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]