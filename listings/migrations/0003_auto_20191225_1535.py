# Generated by Django 2.1.1 on 2019-12-25 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191225_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='realtor', to='realtors.Realtor'),
        ),
    ]