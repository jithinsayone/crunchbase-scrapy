from django.contrib import admin
from .models import People_Crunchbase,Company_Crunchbase
from import_export.admin import ImportExportModelAdmin


class Company_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','category','location')
    search_fields = [ 'name','category','location']

class People_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','company_name','designation','location')
    search_fields = [ 'name','company_name','designation','location']
    list_filter = (
       'company_name', 'designation', 'location',

   )


class PeopleAdmin(ImportExportModelAdmin):
    resource_class = People_Crunchbase

admin.site.register(People_Crunchbase,People_CrunchbaseAdmin,PeopleAdmin)
admin.site.register(Company_Crunchbase,Company_CrunchbaseAdmin)



# Register your models here.
