# Generated by Django 3.2.9 on 2022-01-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_users_wantlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='cart',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]