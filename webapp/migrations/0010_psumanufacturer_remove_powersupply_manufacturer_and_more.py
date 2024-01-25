# Generated by Django 4.2.6 on 2024-01-09 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_rammanufacturer_alter_manufacturer_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PSUManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'PSUmanufacturers',
            },
        ),
        migrations.RemoveField(
            model_name='powersupply',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='powersupply',
            name='PSUmanufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.psumanufacturer'),
        ),
    ]
