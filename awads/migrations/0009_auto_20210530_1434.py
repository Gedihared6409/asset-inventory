# Generated by Django 3.1.6 on 2021-05-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awads', '0008_auto_20210530_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='urgent',
            field=models.CharField(choices=[('Urgent', 'Urgent'), ('Not Urgent', 'Not Urgent')], max_length=200, null=True),
        ),
    ]
