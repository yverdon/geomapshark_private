# Generated by Django 2.2.6 on 2019-10-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0018_department_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArcheoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
            ],
            options={
                'verbose_name': 'archeotype',
            },
        ),
    ]
