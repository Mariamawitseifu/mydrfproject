# Generated by Django 4.2.7 on 2023-12-05 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='username',
        ),
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(default=0.0014829461196243204, on_delete=django.db.models.deletion.CASCADE, to='news.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
