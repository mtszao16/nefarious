# Generated by Django 2.1.5 on 2019-05-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0024_auto_20190306_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='nefarioussettings',
            name='allow_hardcoded_subs',
            field=models.BooleanField(default=False),
        ),
    ]