# Generated by Django 3.2.4 on 2021-07-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0031_add_mandatory_2fa_to_permitdepartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksobjecttype',
            name='notify_services',
            field=models.BooleanField(default=False, verbose_name='Notifier les services'),
        ),
        migrations.AddField(
            model_name='worksobjecttype',
            name='services_to_notify',
            field=models.TextField(blank=True, verbose_name='Emails des services à notifier'),
        ),
    ]
