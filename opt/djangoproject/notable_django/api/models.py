from django.db import models
from django.utils.timezone import now
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Registration(models.Model):
     email_id=models.CharField(max_length=200);
     employee_id=models.CharField(max_length=200);
     phone_number_1=models.CharField(max_length=200);
     phone_number_2=models.CharField(max_length=200);
     name=models.CharField(max_length=200);
     designation=models.CharField(max_length=200);
     pincode=models.CharField(max_length=200);
     status=models.CharField(max_length=200);
     passcode=models.CharField(max_length=200);

     def __str__(self):
         return '%s %s' % (self.email_id, self.employee_id)

class OTP(models.Model):
    lattitude=models.CharField(max_length=200);
    longitude=models.CharField(max_length=200);
    otp=models.CharField(max_length=200);
    timestamp=models.CharField(max_length=200);
    project_id=models.CharField(max_length=200);
    comments=models.CharField(max_length=200);
    employee_id=models.CharField(max_length=200)
    #employee_id=models.ForeignKey('Registration.employee_id', on_delete=models.SET_NULL, null=True)
    shop_code=models.CharField(max_length=8, default="")
    created_at = models.DateTimeField(default=now)
    person=models.ForeignKey('Registration', on_delete=models.SET_NULL, null=True)
    #employee_id=models.ForeignKey('Registration.employee_id', on_delete=models.SET_NULL, null=True)
        #needed to be added
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.employee_id,self.created_at, self.shop_code, self.otp, self.lattitude,self.longitude)

class Shop(models.Model):
    shop=models.CharField(max_length=200);
    shop_longitude=models.CharField(max_length=200);
    shop_lattitude=models.CharField(max_length=200);
    shop_description=models.CharField(max_length=200, default="", editable=False)
