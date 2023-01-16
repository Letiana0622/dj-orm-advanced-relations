from django.contrib import admin
from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_of_true = []
        for form in self.forms:
            list_of_true.append(form.cleaned_data.get('is_main', None))
            if list_of_true.count(True) > 1 or list_of_true.count(True) < 1:
                raise ValidationError('Главный раздел может быть только один')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'text', 'published_at']
    list_filter = ['published_at']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

