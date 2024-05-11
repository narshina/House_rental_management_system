from django.db import models
from tenant.models import Tenant
from owner.models import Owner

# Create your models here.
class PaySecurity(models.Model):
    security_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    card_no = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    add_security_id = models.IntegerField(blank=True, null=True)
    # owner_id = models.IntegerField(blank=True, null=True)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'pay_security'


