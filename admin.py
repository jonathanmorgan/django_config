# import django_config class.
from django_config.models import Config_Property

# import django admin stuff
from django.contrib import admin

# import django db models.
from django import forms
from django.db import models

# start with default admin screens - comment out as we make fancier additions
#    below.
# admin.site.register( Config_Property )

# get fancier

#===============================================================================
# Javascript includes.
#===============================================================================

#default_js = ( '/js/ckeditor/ckeditor.js', '/js/ckeditor/adapters/jquery.js', '/js/ckeditor_config.js' )
default_js = ( '/js/ckeditor_config.js', )

#===============================================================================
# Admin classes
#===============================================================================


#-------------------------------------------------------------------------------
# Issue admin definition
#-------------------------------------------------------------------------------

class Config_PropertyAdmin( admin.ModelAdmin ):

    fieldsets = [
        ( None,
            {
                'fields' : [ 'application', 'property_name', 'property_value' ]
            }
        ),
    ]

    list_display = ( 'id', 'application', 'property_name', 'property_value', )
    list_display_links = ( 'id', 'property_name', )
    list_filter = [ 'application', ]
    search_fields = [ 'application', 'property_name', 'property_value', ]
    # date_hierarchy = 'status_date'
    # actions = [ toggle_published_flag ]
    ordering = [ '-last_update' ]

    # formfield_overrides = { models.TextField: { 'widget' : forms.Textarea( attrs = { 'class' : 'vLargeTextField' } ) }, }

    # class Media:

        #js = ( '/js/ckeditor/ckeditor.js', 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js', '/js/ckeditor/adapters/jquery.js', '/js/ckeditor_config.js', '/js/jqplugins/jquery-autocomplete/jquery.autocomplete.min.js', '/js/django/ajax_select.js', )
        #js = default_js
        #css = {
        #    'all' : ( '/js/jqplugins/jquery-autocomplete/jquery.autocomplete.css', '/js/jqplugins/jquery-autocomplete/iconic.css' )
        #}
        
    #-- END class Media --#

#-- END IssueAdmin admin class --#

admin.site.register( Issue, IssueAdmin )