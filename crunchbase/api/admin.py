from django.contrib import admin
from .models import People_Crunchbase,Company_Crunchbase

class Company_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','category','location')
    search_fields = [ 'name','category','location']

class People_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','company_name','designation','location')
    search_fields = [ 'name','company_name','designation','location']

admin.site.register(People_Crunchbase,People_CrunchbaseAdmin)
admin.site.register(Company_Crunchbase,Company_CrunchbaseAdmin)



# Register your models here.
