from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Parts_Of_Speech)
admin.site.register(Article)
admin.site.register(Jumbled_Sentence)
admin.site.register(Errors_and_Omission)
admin.site.register(Topic)