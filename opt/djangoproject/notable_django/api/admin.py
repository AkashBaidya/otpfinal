from django.contrib import admin
from .models import *

import csv
from django.http import HttpResponse

from .models import Registration

#from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Registration)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class OTPAdmin(admin.ModelAdmin,ExportCsvMixin):
    search_fields = ('employee_id', 'shop_code')
    list_display=('employee_id','created_at','shop_code','otp','lattitude','longitude')
    list_filter = ['created_at','employee_id', 'shop_code']
    actions = ["export_as_csv"]

admin.site.register(OTP,OTPAdmin)


