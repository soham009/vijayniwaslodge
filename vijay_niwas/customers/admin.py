from django.contrib import admin
from django.contrib.auth.models import Group
import csv
from django.http import HttpResponse
from customers.models import NewEntry, passengers

# Register your models here.
admin.site.site_header = "Vijay Niwas Lodge Software"
admin.site.site_title = "Vijay Niwas"
admin.site.index_title = "Welcome, Lets Manage Customer Data with Ease"



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

    export_as_csv.short_description = "Export Excel"

class NewEntryAdmin(admin.ModelAdmin,ExportCsvMixin):
    search_fields = [ "Entry_No","Name_of_Visitor","Room_No","Payment_Status", ]
    list_filter = ["Room_No", "Payment_Status"]
    list_display = [
        "Entry_No",
        "Name_of_Visitor",
        "check_in",
        "check_out",
        "Room_No",
        "Payment_Status",
        
    ]
    list_editable = ["Payment_Status"]
    actions = ["export_as_csv"]

admin.site.register(NewEntry,NewEntryAdmin)
admin.site.unregister(Group)
class passengersAdmin(admin.ModelAdmin,ExportCsvMixin):
    search_fields = ["name","Address", "Age", "Identity_Proof","mobile","Identity_Proof_No",]
    list_display = [
        "name",
        "Address",
        "mobile",
        "Gender", 
        "Age", 
    "Identity_Proof",
    "Identity_Proof_No",

    ]
    actions = ["export_as_csv"]

admin.site.register(passengers,passengersAdmin)
