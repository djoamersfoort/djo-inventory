# Generated by Django 2.1.4 on 2019-01-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20181213_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='properties',
            field=models.ManyToManyField(to='inventory.Property'),
        ),
    ]
