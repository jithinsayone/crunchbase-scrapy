from django.contrib import admin
from .models import People_Crunchbase,Company_Crunchbase

class Company_CrunchbaseAdmin(admin.ModelAdmin):
    list_display=( 'name','category')
    search_fields = [ 'name','category']



admin.site.register(People_Crunchbase)
admin.site.register(Company_Crunchbase,Company_CrunchbaseAdmin)



# Register your models here.
