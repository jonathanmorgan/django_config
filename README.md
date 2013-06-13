# django_config

This is a basic django app that creates a table for configuration settings where each row has the following fields:

- application
- property_name
- property_value

It provides methods for retrieving configuration properties that allow for a default value to be passed in.  This is purposely not all that complicated or sophisticated.  If you want something more robust, there are other, better options.  This is quick and dirty.

## Installation

- make sure south is installed and included in your installed applications.  If not, see below for instructions.

    - install South (data migration tool), if it isn't already installed.
    
            (sudo) pip install South
    
    - in settings.py, add 'south' to the INSTALLED\_APPS list.  Example:
        
            INSTALLED_APPS = (
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                # Uncomment the next line to enable the admin:
                # 'django.contrib.admin',
                # Uncomment the next line to enable admin documentation:
                # 'django.contrib.admindocs',
                'south',
            )
    
    - Once database is configured in settings.py, in your site directory, run "python manage.py syncdb" to create database tables.

- Install django\_config application:

    - Clone code into your django site/project.

            git clone https://github.com/jonathanmorgan/django_config
            
    - use south to install database tables
    
            python manage.py migrate django_config

## License

Copyright 2013 Jonathan Morgan

This file is part of [https://github.com/jonathanmorgan/django_config](https://github.com/jonathanmorgan/django_config).

django_config is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

django_config is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with [https://github.com/jonathanmorgan/django_config](https://github.com/jonathanmorgan/django_config).  If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).