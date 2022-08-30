# Generated by Django 3.2.14 on 2022-07-29 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_serviceprovider_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_skills', to='users.skills'),
        ),
    ]
