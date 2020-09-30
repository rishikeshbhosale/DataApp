from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import villageResource, talukaResource
from .models import taluka, village, visitHistory, login
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter


class loginAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name')
admin.site.register(login, loginAdmin)

class talukaAdmin(ImportExportActionModelAdmin):
    resource_class = talukaResource
    list_display = ('id', 'name')
admin.site.register(taluka, talukaAdmin)

class villageAdmin(ImportExportModelAdmin):
    resource_class = villageResource
    list_display = ('villageName', 'taluka')
    list_filter = (('taluka', RelatedDropdownFilter),)
    search_fields = ('villageName', )
admin.site.register(village, villageAdmin)

class visitHistoryAdmin(ImportExportActionModelAdmin):
    list_display = ('villageName', 'visit_name', 'visit_date', 'visit_reason', 'visit_to_be', 'visit_contact', 'visit_help', 'visit_remark', 'entry_by')
    list_filter = (('villageName', DropdownFilter), ('entry_by', RelatedDropdownFilter),) 
    search_fields = ('visit_date', 'visit_name', )
    # list_filter1 = ('visit_date',)
admin.site.register(visitHistory, visitHistoryAdmin)
 