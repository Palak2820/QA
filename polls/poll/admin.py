from django.contrib import admin

# Register your models here.

from .models import Question,Choice

admin.site.site_header ="Polls Admin"
admin.site.site_title ="Polls Admin Area"
admin.site.index_title ="welcome to Polls Admin Area"


#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class Questionadmin(admin.ModelAdmin):
    fieldsets =[(None,{'fields':['question_text']}),
    ('Date Informaton',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines =[ChoiceInline]
admin.site.register(Question,Questionadmin)


