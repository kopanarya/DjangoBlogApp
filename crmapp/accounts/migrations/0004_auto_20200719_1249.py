# Generated by Django 3.0.6 on 2020-07-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200719_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out of door', 'Out of door')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
