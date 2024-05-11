
from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    pasword = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'