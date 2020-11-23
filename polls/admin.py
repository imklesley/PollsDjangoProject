from django.contrib import admin
from polls.models import Question, Choice

#Título canto superior esquerdo
admin.site.site_header = 'Painel Administrativo'
# admin.site.site_title = 'Área Administrativa'
# admin.site.site_title = 'Bem vindo a área administrativa'


# Register your models here.

# Dessa forma Question e Choice ficam em locais diferentes, sendo dois cadastros a serem feitos
# @admin.register(Question)
# class PollsAdmin(admin.ModelAdmin):
#     list_display = ('question_text', 'pub_date')
#
# @admin.register(Choice)
# class PollsAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'votes')

# Isso fará com que as Choices agora sejam acessadas dentro de QUestions
class ChoiceInLine(admin.TabularInline):
    model = Choice
    # Quantos espaços extra queremos, além do que já existem cadastrados
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
                 # "classes" representa como os fields vão se comportar, no caso irá 'collapsar'
                 ]
    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin)
