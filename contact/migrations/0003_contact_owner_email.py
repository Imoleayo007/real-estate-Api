# Generated by Django 4.1.3 on 2022-12-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner_email',
            field=models.EmailField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
