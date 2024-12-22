from django.db import models

# Create your models here.
class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField()
    description = models.CharField(max_length=45)
    image = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'work'
