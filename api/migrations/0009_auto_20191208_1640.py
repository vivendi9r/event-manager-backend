# Generated by Django 2.2.7 on 2019-12-08 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191208_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Owner'),
        ),
    ]
