from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField()
    consumer_id = models.IntegerField()
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=45)
    date = models.DateField()
    reply = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaint'
