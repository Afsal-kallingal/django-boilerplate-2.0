# Generated by Django 5.0.1 on 2024-01-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_account", "0003_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country_code",
            field=models.CharField(blank=True, default=91, max_length=5, null=True),
        ),
    ]