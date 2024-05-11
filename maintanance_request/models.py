from django.db import models
from tenant.models import Tenant
from owner.models import Owner
from property.models import Property

# Create your models here.
class MaintananceRequest(models.Model):
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # owner_id = models.IntegerField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    # house_id = models.IntegerField()
    house=models.ForeignKey(Property, on_delete=models.CASCADE)
    maintanance = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    maintanance_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'maintanance_request'


