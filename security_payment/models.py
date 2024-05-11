from django.db import models
from owner.models import Owner
from tenant.models import Tenant
from property.models import Property

# Create your models here.
class SecurityPayment(models.Model):
    # owner_id = models.IntegerField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # house_id = models.IntegerField()
    house=models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.IntegerField()
    duedate = models.CharField(max_length=45)
    add_security_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'security_payment'

