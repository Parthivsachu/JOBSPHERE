from django.db import models

# Create your models here.
class Comment(models.Model):
    consumer_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    date = models.DateField()
    provider_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'