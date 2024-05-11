from django.db import models
from owner.models import Owner
from tenant.models import Tenant
# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    # owner_id = models.CharField(max_length=45)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    notification = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'notification'

