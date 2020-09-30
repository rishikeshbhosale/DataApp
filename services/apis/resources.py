from import_export import resources
from .models import taluka, village
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter

class talukaResource(resources.ModelResource):
    class Meta:
        model = taluka
        exclude = ('id',)
        import_id_fields = ('name',)
        MAX_UPLOAD_SIZE = "5242880"

class villageResource(resources.ModelResource):
    class Meta:
        model = village
        exclude = ('id',)
        import_id_fields = ('villageName', 'taluka')