# Generated by Django 4.1.7 on 2023-02-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_application_job_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='commentary',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_contact',
            field=models.DateField(default=None, null=True),
        ),
    ]
