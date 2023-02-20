from django.db import models

# Create your models here.


class Application(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    stage = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    app_date = models.DateField()
    last_contact = models.DateField(null=True)
    job_description = models.TextField(max_length=10000000)
    commentary = models.CharField(max_length=10000, null=True)
    contact = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'application'
