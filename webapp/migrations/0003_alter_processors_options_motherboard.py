# Generated by Django 4.2.6 on 2023-12-02 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_alter_category_options_processors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processors',
            options={'verbose_name_plural': 'processors'},
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=200)),
                ('productcode', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('prodsupplier', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.SET_NULL, to='webapp.category')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]