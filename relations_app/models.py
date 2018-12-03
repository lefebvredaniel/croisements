from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Documents(models.Model):
       documents_adresse  = models.URLField()
       documents_commentaires = models.CharField(max_length=1000)
       
       def __str__(self):
            return self.documents_adresse

       class meta:
            ordering =['id']


class Artiste(models.Model):


    artiste_nom = models.CharField(max_length=70)
    artiste_prénom = models.CharField(max_length=70)
    artiste_datenaissance = models.DateField(max_length=50)
    artiste_datedeces = models.DateField(max_length=50)
    artiste_wiki = models.URLField(blank=True)
    artiste_biolight=models.CharField(max_length=500,blank=True)
    artiste_nomjpg=models.CharField(max_length=500,default='nom_artiste')
    
    

    def __str__(self):
         return self.artiste_nom
    pub_date = models.DateTimeField('date published',auto_now_add=True)


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




class Commentaires(models.Model):

    author = models.ForeignKey (User,
        on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    titre = models.ForeignKey (Documents, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class R_artiste_documents(models.Model):
   artiste_nom = models.ForeignKey(Artiste, on_delete=models.CASCADE)
   documents_adresse=models.ForeignKey(Documents, on_delete=models.CASCADE)
   
   



