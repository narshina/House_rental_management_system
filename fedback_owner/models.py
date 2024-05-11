from django.db import models
from tenant.models import Tenant
from owner.models import Owner
from property.models import Property

# Create your models here.


class FeedbackOwner(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # tenant_id = models.CharField(max_length=45)
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # owner_id = models.IntegerField()
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    # house_id = models.IntegerField()
    house=models.ForeignKey(Property,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'feedback_owner'




