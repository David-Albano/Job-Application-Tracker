# Generated by Django 4.1.7 on 2023-02-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_application_commentary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='last_contact',
            field=models.DateField(null=True),
        ),
    ]
