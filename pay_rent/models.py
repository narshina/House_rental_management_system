from django.db import models
from tenant.models import Tenant
from owner.models import Owner
from rent_payment.models import RentPayment
# Create your models here.
class PayRent(models.Model):
    rent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    card_no = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # owner_id = models.IntegerField(blank=True, null=True)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    add_rent_id = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'pay_rent'



