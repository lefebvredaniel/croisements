from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url



app_name = 'relations_app'



urlpatterns = [
    path('', views.index, name='index'),


    
 #    path('apropos', views.apropos, name='apropos'),
    path('<int:artiste_id>/connexion/',views.connexion, name='connexion'),
    path('<int:id_artiste>/<int:id_artisteS>/liste_documents/',views.liste_documents, name='liste_documents'),
    #path('<int:id_doc>/documents/',views.documents, name='documents'),
 #    path('poursyretrouver',views.poursyretrouver, name='poursyretrouver'),
 #    path('poursyretrouverFREQ',views.poursyretrouverFREQ, name='poursyretrouverFREQ'),
 #    path('liensinteressants',views.liensinteressants, name='liensinteressants'),
 #    path('grammaire',views.grammaire, name='liensinteressants'),
 #    path('mescommentaires',views.mescommentaires, name='mescommentaires'),
 #    path('<int:id>/mescommentaires/asupprimer',views.supprimer, name='supprimer'),
 #    path('<int:id>/mescommentaires/amodifier',views.modifier, name='modifier'),
 # #   path('message',views.message, name='message'),
 #    path('recherche', views.recherche, name='recherche'),
 #    path('recherche1', views.recherche1, name='recherche1'),
 #    path ('contact',views.contact,name='contact'),
 #    path('commentaires_list',CommentairesListView.as_view(),name="ProductListView"),
 #    path('<int:id>/<int:titre_id>/mescommentaires/asupprimer1',views.supprimer1, name='supprimer1'),
 #    path('<int:id>/mescommentaires/amodifier1',views.modifier1, name='modifier1'),






]
"""
Example URLConf for a contact form.
If all you want is the basic ContactForm with default behavior,
include this URLConf somewhere in your URL hierarchy (for example, at
``/contact/``)
"""





##urlpatterns = [
##    url('contact/',
##        views.ContactFormView.as_view(),
##        name='contact'),
####    url(r'^sent/$',
####        TemplateView.as_view(
####            template_name='contact_form/contact_form_sent.html'),
####        name='contact_form_sent'),
##]
