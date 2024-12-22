from django.db import models

# Create your models here.
class Skill(models.Model):
    consumer_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'skill'
