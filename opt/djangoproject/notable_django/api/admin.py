from django.contrib import admin
from .models import *

from django import forms
from django.urls import path

import csv
from django.http import HttpResponse

from .models import Registration
from .models import OTP

from django.conf.urls import url, include

from import_export.admin import ImportExportModelAdmin

#from import_export.admin import ImportExportModelAdmin

# Register your models here.

# class CsvImportForm(forms.Form):
#     csv_file = forms.FileField()



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


# admin.site.register(Registration)
@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    pass
# @admin.register(OTP)
# class OTPAdmin(ImportExportModelAdmin):
#     pass

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin,ExportCsvMixin):
    search_fields = ('employee_id', 'shop_code')
    list_display=('employee_id','created_at','shop_code','otp','lattitude','longitude')
    list_filter = ['created_at','employee_id', 'shop_code']
    actions = ["export_as_csv","CSV UPLOAD"]

    # change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            # Create Hero objects from passed in data
            # ...
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

# admin.site.register(OTP,OTPAdmin)
