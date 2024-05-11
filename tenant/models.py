from django.db import models

# Create your models here.
class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    tenant_name = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    house_name = models.CharField(max_length=45)
    landmark = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    mob_no = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    id_proof = models.CharField(max_length=200)
    professional_id = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    marriage = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)



    class Meta:
        managed = False
        db_table = 'tenant'




