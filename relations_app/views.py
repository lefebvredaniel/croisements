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

from relations_app.forms import RechercheForm, CommentForm, ContactForm
from django.utils import timezone
from django.core.mail import send_mail
from django.views.generic import ListView
from relations_app.models import Artiste, Documents,R_artiste_documents, Commentaires
from django.db.models import Q
from django.db.models import F
from django.db.models.functions import Extract
"""
View which can render and send email from a contact form.
"""
from datetime import datetime,date

try:
    from django.urls import reverse
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import reverse  # pragma: no cover

def index(request):


#On affiche toutes les étiquettes en les classant par fréquence (le comptage se fait avec la table relation R_Extraits_Etiquettes) puis par ordre alphabétique

    # titre_list=Extraits.objects.all()
    liste_artiste=Artiste.objects.all().order_by('artiste_nom')


    context={'dict_artiste':liste_artiste}

    return render(request, 'relations_app/index.html',context)

def indexnaiss(request):
   
    liste_artiste=Artiste.objects.all().order_by('artiste_datenaissance')
    

    context={'dict_artiste':liste_artiste}
    return render(request, 'relations_app/index.html',context)

def indexdeces(request):
    liste_artiste=Artiste.objects.all().order_by('artiste_datedeces')


    context={'dict_artiste':liste_artiste}
    return render(request, 'relations_app/index.html',context) 

def longevite(request):
    # liste_artiste=Artiste.objects.all().order_by('artiste_datenaissance')

    # dict_longevite={}
    
    # for indice in liste_artiste:
    #     dico={}
        
    #     mois_naissance=str(indice.artiste_datenaissance)[5:7]
    #     mois_deces=str(indice.artiste_datedeces)[5:7]
        
       
    #     annee_naissance=str(indice.artiste_datenaissance)[:4]
    #     annee_deces=str(indice.artiste_datedeces)[:4]
    #     age=(int(annee_deces)*12+int(mois_deces)-int(annee_naissance)*12-int(mois_naissance))//12
        
    #     annee2chiffres=int(annee_naissance)-1800
    #     dico[age]=(annee2chiffres//10)
       
    #     dict_longevite[indice.artiste_nom]=(dico)
    #     # dict_longevite2[indice.artiste_nom]=(annee2chiffres)
        
    
    liste_artiste=Artiste.objects.annotate (age=(Extract('artiste_datedeces','year')*12+Extract('artiste_datedeces','month')-
        Extract('artiste_datenaissance','year')*12-Extract('artiste_datenaissance','month'))/12).annotate(anaiss2=(Extract('artiste_datenaissance','year')-1800)).annotate(anaiss4=Extract('artiste_datenaissance','year')).annotate(adeces4=Extract('artiste_datedeces','year')).order_by('artiste_datenaissance')
    
    context={'dictionnaire_longevite':liste_artiste}

    

    return render(request, 'relations_app/longevite.html',context)
    





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

    return render(request,'relations_app/connexion.html',context)


def liste_documents(request,id_artisteS,id_artiste):
    

    dico_liste_documents={}
    liste_documents=R_artiste_documents.objects.filter(artiste_nom_id=id_artisteS)
    
   
    for i in liste_documents:

        filtre=i.documents_adresse_id
        liste_connexion=R_artiste_documents.objects.filter(documents_adresse_id=filtre)
        
        for j in liste_connexion:

            if j.artiste_nom_id==id_artiste:
                    le_document=Documents.objects.filter(id=j.documents_adresse_id)
                    
                    dico_liste_documents[j.documents_adresse_id]=le_document
                        
    

    # criterion1 = Q(id__contains=id_artiste)
    # criterion2 = Q(id__contains=id_artisteS)

    nom_artiste = Artiste.objects.filter(Q(id__exact=id_artiste) | Q(id__exact=id_artisteS))
    



    context={'dico_liste_documents':dico_liste_documents,'nom_artiste':nom_artiste}
   


    return render(request,'relations_app/liste_documents.html',context)

def apropos (request):
    context={}
    return render(request,'relations_app/apropos.html', context)

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)

    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.

    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']

        renvoi = form.cleaned_data['renvoi']
        send_mail(sujet,message+"    "+envoyeur, envoyeur,['dlemproust@gmail.com'],fail_silently=False)


        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        if renvoi:
            send_mail("copie de votre message"+"   " +sujet,message,'dlemproust@gmail.com',[envoyeur],fail_silently=False)
        envoi = True
    form=ContactForm()

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'relations_app/contact.html', locals())

def work(request):
    dict_liste_artiste={}
    # extraits_list=Extraits.objects.annotate(nb1=Count('commentaires'))

    liste_artiste=Artiste.objects.annotate(nb1=Count('r_artiste_documents')).order_by('nb1')
    # for i in range(len(liste_artiste)):
    #     # dict_liste_artiste[i.artiste_nom]=str(i.nb1)
    #     print(liste_artiste[i].artiste_nom, liste_artiste[i].nb1)
    

       
    context={'dict_liste_artiste':liste_artiste}
   


    return render(request, 'relations_app/work.html', context)


# Create your views here.
