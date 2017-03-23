from django.contrib import admin
from .models import People_Crunchbase,Company_Crunchbase
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class People_CrunchbaseResource(resources.ModelResource):

    class Meta:
        model = People_Crunchbase

class Company_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','category','location')
    search_fields = [ 'name','category','location']

class People_CrunchbaseAdmin(ImportExportModelAdmin):
   #  list_display=( 'name')#,'company_name','designation','location')
   #  # search_fields = [ 'name','company_name','designation','location']
   #  list_filter = (
   #     'company_name', 'designation', 'location',
   #
   # )
   pass


class PeoplecrunchProxy(admin.ModelAdmin):
    list_display=( 'name','company_name','designation','location')
    search_fields = [ 'name','company_name','designation','location']
    list_filter = (
       'company_name', 'designation', 'location',

   )
    resource_class = People_CrunchbaseResource


admin.site.register(People_Crunchbase,People_CrunchbaseAdmin)
admin.site.register(Company_Crunchbase,Company_CrunchbaseAdmin)
admin.site.register(People_Crunchbase,PeoplecrunchProxy)



# Register your models here.
