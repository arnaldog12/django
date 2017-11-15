from django.contrib import admin

# Register your models here.
from .models import Choice, Question

'''
admin.StackedInline: Empilha os campos do modelo Choice
admin.TabularInline: Coloca os campos do modelos Choice em uma única linha
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # define a ordem que os campos aparecem

    # divide o formulário em grupos
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]

# usuário: admin senha: adminadmin
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)