# Generated by Django 2.2.3 on 2019-07-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190704_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
