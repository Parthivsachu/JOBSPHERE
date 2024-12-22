from django.db import models

# Create your models here.
class Consumer(models.Model):
    consumer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact = models.IntegerField()
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'consumer'
