from django.db import models

# Create your models here.
class Provider(models.Model):
    provider_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    address = models.CharField(max_length=75)
    contact = models.CharField(max_length=45)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'provider'
