# coding: utf-8
from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.db.models import Count
#from digressions.models import Extraits, Etiquettes,R_Extraits_Etiquettes, Commentaires

from django.urls import reverse
from django.contrib.auth.models import User
# from django.db import connection

#from digressions.forms import RechercheForm, CommentForm, ContactForm
from django.utils import timezone
from django.core.mail import send_mail
from django.views.generic import ListView
from relations_app.models import Artiste, Documents,R_artiste_documents, Commentaires
from django.db.models import Q
"""
View which can render and send email from a contact form.
"""

try:
    from django.urls import reverse
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import reverse  # pragma: no cover

def index(request):


#On affiche toutes les étiquettes en les classant par fréquence (le comptage se fait avec la table relation R_Extraits_Etiquettes) puis par ordre alphabétique

    # titre_list=Extraits.objects.all()
    liste_artiste=Artiste.objects.all()
    
   
    context={'dict_artiste':liste_artiste}

    return render(request, 'relations_app/index.html',context)

def connexion(request, artiste_id):
    nom_selectionne=Artiste.objects.filter(id=artiste_id)

    
    dico={}
    
    liste_documents=R_artiste_documents.objects.filter(artiste_nom_id=artiste_id)
  
    for i in liste_documents:
        filtre=i.documents_adresse_id
        
        liste_connexion=R_artiste_documents.objects.filter(documents_adresse_id=filtre)
        for j in liste_connexion:
            if j.artiste_nom!=i.artiste_nom:
                dico[j.artiste_nom]=j.artiste_nom
    
   
 

    context={'dico': dico,'nom_selectionne':nom_selectionne}
    print(context)
    return render(request,'relations_app/connexion.html',context)

def liste_documents(request,id_artisteS,id_artiste):
    dico_liste_documents={}
    liste_documents=R_artiste_documents.objects.filter(artiste_nom_id=id_artisteS) 
    
    for i in liste_documents:
        filtre=i.documents_adresse_id
        liste_connexion=R_artiste_documents.objects.filter(documents_adresse_id=filtre)
        for j in liste_connexion:
           
            if j.artiste_nom_id==id_artiste:
                        dico_liste_documents[j.documents_adresse_id]=j.documents_adresse
    

    criterion1 = Q(id__contains=id_artiste)
    criterion2 = Q(id__contains=id_artisteS)

    nom_artiste = Artiste.objects.filter(criterion1 | criterion2)
    print(nom_artiste)


    context={'dico_liste_documents':dico_liste_documents,'nom_artiste':nom_artiste}
    print(context)
    return render(request,'relations_app/liste_documents.html',context)



# Create your views here.
