# Generated by Django 4.1.4 on 2022-12-24 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_uuid_cart_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]
