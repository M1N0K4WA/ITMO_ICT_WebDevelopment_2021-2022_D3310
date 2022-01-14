# Generated by Django 3.2.9 on 2022-01-12 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsimage',
            name='goods_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userAddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userAvatar',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userEmail',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userNickName',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userPhone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='users',
            name='userPassword',
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='GoodsImage',
        ),
    ]