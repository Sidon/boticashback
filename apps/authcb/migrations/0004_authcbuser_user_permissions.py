# Generated by Django 3.0.3 on 2020-02-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('authcb', '0003_authcbuser_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='authcbuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission'),
        ),
    ]
