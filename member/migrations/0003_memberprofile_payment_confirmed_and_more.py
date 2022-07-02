# Generated by Django 4.0.4 on 2022-06-29 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0002_remove_memberprofile_name_memberprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberprofile',
            name='payment_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
