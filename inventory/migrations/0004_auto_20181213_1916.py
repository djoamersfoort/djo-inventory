# Generated by Django 2.1.4 on 2018-12-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20181213_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='photo',
            field=models.BinaryField(editable=True, max_length=2000000, null=True),
        ),
    ]
