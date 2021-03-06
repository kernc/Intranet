#!/usr/bin/env python
# -*- coding: utf-8 -*-

from intranet.org.models import *
from django.contrib import admin
from reversion.admin import VersionAdmin
from tinymce.widgets import TinyMCE
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class SodelovanjeAdmin(VersionAdmin):
    search_fields = ('person__name',)
    list_filter = ('tip',)


class DiaryAdmin(VersionAdmin):
    search_fields = ['log_formal', 'person', 'task']
    date_hierarchy = 'date'
    list_filter = ['date', 'task', 'author']
    list_display = ('date', 'author', 'task', 'length')

    class Media:
        js = ('js/tags.js',)


class PersonAdmin(VersionAdmin):
    ordering = ('name',)
    search_fields = ('name',)


class EventAdmin(VersionAdmin):
    search_fields = ['title']
    date_hierarchy = 'start_date'
    ordering = ['-start_date']
    list_filter = ['project', 'start_date']
    list_display = ['title', 'start_date', 'end_date']

    class Media:
        js = ('js/tags.js',)


class StickyNoteAdmin(VersionAdmin):
    search_fields = ['note']
    date_hierarchy = 'due_date'
    list_filter = ['due_date', 'author']

    class Media:
        js = ('js/tags.js',)


class LendAdmin(VersionAdmin):
    search_fields = ['to_who', 'why', 'note']
    list_display = ['what', 'returned', 'from_who', 'to_who', 'from_date', 'due_date', 'why']


class ScratchpadAdmin(VersionAdmin):
    get_latest_by = "id"


class ProjectAdmin(VersionAdmin):
    search_fields = ['note', 'name', 'responsible']
    list_display = ['name', 'responsible', 'parent', 'note']
    js = ('js/tags.js',)


class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE())
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(Category)
admin.site.register(TipSodelovanja)
admin.site.register(Place)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Organization)
admin.site.register(Shopping)
admin.site.register(IntranetImage)
admin.site.register(Sodelovanje, SodelovanjeAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Lend, LendAdmin)
admin.site.register(StickyNote, StickyNoteAdmin)
admin.site.register(Scratchpad, ScratchpadAdmin)
admin.site.register(Project, ProjectAdmin)
