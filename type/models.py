from django.db import models
from owner.models import Owner

# Create your models here.
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    # owner_id = models.IntegerField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'type'

