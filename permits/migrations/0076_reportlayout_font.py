# Generated by Django 3.2.13 on 2022-05-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0075_auto_20220530_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportlayout',
            name='font',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
