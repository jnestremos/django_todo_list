# Generated by Django 3.2.6 on 2021-09-28 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pricing',
            field=models.DecimalField(decimal_places=2, max_digits=200, null=True),
        ),
    ]
