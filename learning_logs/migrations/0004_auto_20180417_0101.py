# Generated by Django 2.0.4 on 2018-04-17 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
    ]
