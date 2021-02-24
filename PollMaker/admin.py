from django.contrib import admin

from .models import PollQuestion, PollAnswer

class ChoiceInline(admin.TabularInline):
    model = PollAnswer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']})]
    inlines = [ChoiceInline]

admin.site.register(PollQuestion, QuestionAdmin)

