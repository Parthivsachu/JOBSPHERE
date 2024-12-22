from django.db import models

# Create your models here.
class Labour(models.Model):
    labour_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    address = models.CharField(max_length=75)
    contact = models.CharField(max_length=45)
    email = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'labour'
