from django.contrib import admin
from .models import People_Crunchbase,Company_Crunchbase

class Company_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','category','location')
    search_fields = [ 'name','category','location']

class People_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','company_name','designation','location')
    search_fields = [ 'name','company_name','designation','location']
    list_filter = (
       'company_name', 'designation', 'location',

   )

    def has_csv_permission(self, request):
        """Only super users can export as CSV"""
        if request.user.is_superuser:
            return True

admin.site.register(People_Crunchbase,People_CrunchbaseAdmin)
admin.site.register(Company_Crunchbase,Company_CrunchbaseAdmin)



# Register your models here.
