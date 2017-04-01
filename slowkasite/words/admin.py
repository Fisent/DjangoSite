from django.contrib import admin

from .models import Word

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['word_pol']}),
                 ('Tlumaczenie angielskie', {'fields' : ['word_eng']}),
                 ('Poziom znajomosci', {'fields' : ['word_level']})
                 ]

admin.site.register(Word, QuestionAdmin)


# Register your models here.
