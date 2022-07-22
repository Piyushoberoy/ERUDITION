from urllib import request
from django.urls import path
from requests import post
from READING import views
from READING.models import *
subtopic = SubTopic.objects.all()
urlpatterns = [
    path('',views.INDEX),
    path('Nouns',views.NOUN, name="Nouns"),
    path('Pronouns',views.PRONOUN, name="Pronouns"),
    path('Verbs',views.VERB, name="Verbs"),
    path('Adjectives',views.ADJECTIVE, name="Adjectives"),
    path('Adverbs',views.ADVERB, name="Adverbs"),
    path('Prepositions',views.PREPOSITION, name="Prepositions"),
    path('Conjunctions',views.CONJUNCTION, name="Conjunctions"),
    path('Interjections',views.INTERJECTION, name="Interjections"),
    path('A',views.A, name="A"),
    path('An',views.AN, name="An"),
    path('The',views.THE, name="The")
]