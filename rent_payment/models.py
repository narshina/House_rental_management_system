from django.db import models
from owner.models import Owner
from tenant.models import Tenant
from property.models import Property

# Create your models here.
class RentPayment(models.Model):
    # owner_id = models.IntegerField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    # tenant_id = models.IntegerField()
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # house_id = models.IntegerField()
    house=models.ForeignKey(Property,on_delete=models.CASCADE)
    due_date = models.DateField(db_column='due date')  # Field renamed to remove unsuitable characters.
    add_rent_id = models.AutoField(primary_key=True)
    rent_amount = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'rent_payment'




