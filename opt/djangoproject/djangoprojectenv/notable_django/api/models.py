from django.db import models

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
