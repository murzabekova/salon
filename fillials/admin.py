from django.contrib import admin
from fillials.models import Fillials, Gallery
from fillials.forms import FillialsForm

# Register your models here.


class Fillials_gallery(admin.StackedInline):
    model = Gallery
    extra = 1


@admin.register(Fillials)
class FillialsAdmin(admin.ModelAdmin):
    form = FillialsForm
    fields = ('title', 'description', 'image')
    inlines = [Fillials_gallery]
    # list_filter = ['created_at']
