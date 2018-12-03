from django.contrib import admin
from django.contrib import admin

from .models import Artiste


from .models import Documents

from .models import R_artiste_documents


class ChoixArtiste(admin.TabularInline):

	model=R_artiste_documents
	fields=['artiste_nom']

class DocumentsAdmin(admin.ModelAdmin):
    
    
	inlines = [ChoixArtiste]

class ArtisteAdmin(admin.ModelAdmin):

  	

    
    
    search_fields =['artiste_nom']
    fields=['pub_date', 'artiste_nomjpg']
    
    
 
	
    


	
   

admin.site.register(Documents, DocumentsAdmin)


admin.site.register(Artiste)

admin.site.register(R_artiste_documents)

# Register your models here.