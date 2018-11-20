from django.contrib import admin
from django.contrib import admin

from .models import Artiste


from .models import Documents

from .models import R_artiste_documents


class ChoixDocuments(admin.TabularInline):
    model = R_artiste_documents


class ArtisteAdmin(admin.ModelAdmin):

  	

    fields=['artiste_nom']
    
    search_fields =['artiste_nom']
 

    inlines = [ChoixDocuments]
   

admin.site.register(Documents)


admin.site.register(Artiste)

admin.site.register(R_artiste_documents)

# Register your models here.