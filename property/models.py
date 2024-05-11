from django.db import models
from owner.models import Owner
from type.models import Type

# Create your models here.
class Property(models.Model):
    house_id = models.AutoField(primary_key=True)
    # owner_id = models.CharField(max_length=45)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=45)
    # owner_name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    landmark = models.CharField(max_length=100)
    number_of_bedrooms = models.CharField(max_length=45)
    area_of_house = models.CharField(max_length=45)
    image1 = models.CharField(max_length=200)
    image2 = models.CharField(max_length=200)
    security_payment = models.CharField(max_length=45)
    rent_amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    contact_no = models.CharField(max_length=45)
    # type_id = models.IntegerField()
    type=models.ForeignKey(Type, on_delete=models.CASCADE)
    block = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'property'


