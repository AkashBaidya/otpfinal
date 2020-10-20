from tastypie.resources import ModelResource
from api.models import Note
from api.models import Registration
from api.models import OTP
from api.models import Shop

# import Random

from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        

class RegistrationResource(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='registration'

        fields = ['email_id', 'employee_id','phone_number_1','phone_number_2','name']
        filtering = {
                    'employee_id': ['exact'],
        }
      
#---------------Chcek Phone Number------------------------
#Returns name and designation if valid, else return nothing


class CheckPhoneNumberResource(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='phone'
        #fields = ['name','designation']
        excludes=['name','designation']
        filtering = {
            'phone_number_2': ['exact'],
            'phone_number_1': ['exact'],
            'employee_id': ['exact']
        }


       
       
#---------------Chcek Passcode------------------------
#Returns all if valid, else return nothing

class CheckPasscodeResource(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='passcode'
        #fields = ['name','designation','phone_number_1']
        filtering = {
            'passcode': ['exact'],
            'employee_id': ['exact'],
            'phone_number_1': ['exact'],
            'phone_number_2': ['exact'],
        }

    def dehydrate(self, bundle):
        bundle.data['designation']=bundle.data['designation'].lower()
        return bundle

#---------------Chcek Pincode------------------------
#Returns all if valid, else return nothing

class CheckPasscodeResource(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='passcode'
        #fields = ['name','designation','phone_number_1']
        filtering = {
            'pincode': ['exact'],
            'employee_id': ['exact'],
            'phone_number_1': ['exact'],
            'phone_number_2': ['exact'],
        }

    def dehydrate(self, bundle):
        bundle.data['designation']=bundle.data['designation'].lower()
        return bundle 


#---------------Enter Registration data------------------------
#Returns all if valid, else return nothing

class EnterRegistrationData(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='enter'
        authorization = Authorization()
        #authorization = DjangoAuthorization()
        #authentication = OAuth20Authentication()
        allowed_methods = ['post','get']
        # fields = ['name','designation','phone_number_1']
   

    # def dehydrate(self, bundle):
    #     bundle.data['designation']=bundle.data['designation'].lower()
    #     return bundle                    

#---------------Enter Registration data------------------------
#Returns all if valid, else return nothing

class OtpGenerationResource(ModelResource):
    class Meta:
        queryset=OTP.objects.all()
        resource_name='otp'
        authorization = Authorization()
        #authorization = DjangoAuthorization()
        #authentication = OAuth20Authentication()
        allowed_methods = ['post','get']
        filtering = {
                    'otp': ['exact'],
        }

#----lagbe -----------Enter otp verify-----------------------
#Returns all if valid, else return nothing

class OtpVerifyResource(ModelResource):
    class Meta:
        queryset=OTP.objects.all()
        resource_name='verify'
        filtering = {
                    'otp': ['exact'],
        }

#----lagbe -----------Enter otp verify-----------------------
#Returns all if valid, else return nothing

class ShopResource(ModelResource):
    class Meta:
        queryset=Shop.objects.all()
        resource_name='shop'
        filtering = {
                    'shop': ['exact'],
        }
   

    # def dehydrate(self, bundle):
    #     bundle.data['designation']=bundle.data['designation'].lower()

    #     return bundle 
        

    # def dehydrate(self, bundle):
    #     #random=Random.randomStringDigits
    #     bundle.data['otp']=randomStringDigits(8)

    #     return bundle 


# print ("Generating a Random String including letters and digits")
# print ("First Random String is  ", randomStringDigits(8))
# print ("Second Random String is ", randomStringDigits(8))
# print ("Third Random String is  ", randomStringDigits(8))

