# Generated by Django 2.2.5 on 2020-12-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201204_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_comfirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
