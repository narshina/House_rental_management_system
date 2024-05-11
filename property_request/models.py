from django.db import models
from property.models import Property
from tenant.models import Tenant
from owner.models import Owner

# Create your models here.
class PropertyRequest(models.Model):
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # house_id = models.IntegerField()
    house=models.ForeignKey(Property, on_delete=models.CASCADE)
    required_year = models.CharField(max_length=45)
    required_month = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    request_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    # owner_id = models.IntegerField(blank=True, null=True)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'property_request'
