# Generated by Django 3.2.4 on 2021-06-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_alter_filesadmin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesadmin',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]