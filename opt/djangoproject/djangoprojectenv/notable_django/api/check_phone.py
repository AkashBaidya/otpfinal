from tastypie.resources import ModelResource
from api.models import Note
from api.models import Registration


class CheckPhoneNumberResource(ModelResource):
    class Meta:
        queryset=Registration.objects.all()
        resource_name='phone'
        #fields = ['name','designation']
        excludes=['name','designation']
        filtering = {
            'phone_number_2': ['exact']
        }