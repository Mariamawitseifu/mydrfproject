# Generated by Django 4.2.7 on 2023-12-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('superadmin', 'Superadmin'), ('manager', 'Manager'), ('user', 'User'), ('graphicsdesigner', 'Graphicsdesigner')], default='user', max_length=20, null=True),
        ),
    ]
