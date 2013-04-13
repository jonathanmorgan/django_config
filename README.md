# django_config

This is a basic django app that creates a table for configuration settings where each row has the following fields:
- application
- property_name
- property_value

To install, add django_config to INSTALLED_APPS, then run "python manage.py syncdb".

It provides methods for retrieving configuration properties that allow for a default value to be passed in.  This is purposely not all that complicated or sophisticated.  If you want something more robust, there are other, better options.  This is quick and dirty.
