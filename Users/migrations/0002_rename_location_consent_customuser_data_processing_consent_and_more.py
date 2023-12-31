# Generated by Django 4.2.6 on 2023-12-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='location_consent',
            new_name='data_processing_consent',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='marketing_consent',
            new_name='newsletter_consent',
        ),
        migrations.AddField(
            model_name='customuser',
            name='terms_consent',
            field=models.BooleanField(default=False),
        ),
    ]
