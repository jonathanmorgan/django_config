from django.core.management.base import BaseCommand, CommandError
from django_config.models import Config_Property

class Command( BaseCommand ):

    # CONSTANTS-ish

    # param names
    PARAM_NAME_APP = Config_Property.PARAM_NAME_APP
    PARAM_NAME_GROUP = Config_Property.PARAM_NAME_GROUP
    PARAM_NAME_NAME = Config_Property.PARAM_NAME_NAME
    PARAM_NAME_VALUE = Config_Property.PARAM_NAME_VALUE

    help = 'Accepts information needed to set a configuration property in the database.'
    help += '\nParameters:'
    help += '\n- --{}: Name of application you want the property to be stored under. Defaults to {}'.format( Config_Property.PARAM_NAME_APP, Config_Property.APPLICATION_DEFAULT )
    help += '\n- --{}: Property group you want property to be included in. Defaults to {}'.format( Config_Property.PARAM_NAME_GROUP, Config_Property.PROP_GROUP_DEFAULT )
    help += '\n- --{}: (required) Name of property you want to set.'.format( Config_Property.PARAM_NAME_NAME )
    help += '\n- --{}: Value you want property to be set to. If not provided, sets property to None.'.format( Config_Property.PARAM_NAME_VALUE )
    help += '\n\nAs long as all required information is present, creates or updates property in config table.'

    def add_arguments( self, parser ):

        # application
        parser.add_argument( "--{}".format( Config_Property.PARAM_NAME_APP ) )

        # property group
        parser.add_argument( "--{}".format( Config_Property.PARAM_NAME_GROUP ) )

        # property name
        parser.add_argument( "--{}".format( Config_Property.PARAM_NAME_NAME ) )

        # property value
        parser.add_argument( "--{}".format( Config_Property.PARAM_NAME_VALUE ) )

    #-- END add_arguments() --#

    def handle( self, *args, **options ):

        # declare variables
        my_prop_app = None
        my_prop_group = None
        my_prop_name = None
        my_prop_value = None

        # retrieve options
        my_prop_app = options.get( Config_Property.PARAM_NAME_APP, Config_Property.APPLICATION_DEFAULT )
        my_prop_group = options.get( Config_Property.PARAM_NAME_GROUP, Config_Property.PROP_GROUP_DEFAULT )
        my_prop_name = options.get( Config_Property.PARAM_NAME_NAME, None )
        my_prop_value = options.get( Config_Property.PARAM_NAME_VALUE, None )

        # defaults
        if ( my_prop_app is None ):

            # set it to default application.
            my_prop_app = Config_Property.APPLICATION_DEFAULT

        #-- END check if app is empty. --#

        if ( my_prop_group is None ):

            # set it to default application.
            my_prop_group = Config_Property.PROP_GROUP_DEFAULT

        #-- END check if app is empty. --#

        self.stdout.write( "setting configuration property:" )
        self.stdout.write( "- {prop_name} = {prop_value}".format( prop_name = Config_Property.PARAM_NAME_APP, prop_value = my_prop_app ) )
        self.stdout.write( "- {prop_name} = {prop_value}".format( prop_name = Config_Property.PARAM_NAME_GROUP, prop_value = my_prop_group ) )
        self.stdout.write( "- {prop_name} = {prop_value}".format( prop_name = Config_Property.PARAM_NAME_NAME, prop_value = my_prop_name ) )
        self.stdout.write( "- {prop_name} = {prop_value}".format( prop_name = Config_Property.PARAM_NAME_VALUE, prop_value = my_prop_value ) )

        # must have a name (no value = set to empty)
        if ( ( my_prop_name is not None ) and ( my_prop_name != "" ) ):

            # OK, got what we need. Set the property.
            Config_Property.set_property_value(
                application_IN = my_prop_app,
                property_name_IN = my_prop_name,
                value_IN = my_prop_value,
                property_group_IN = my_prop_group
            )

            self.stdout.write( self.style.SUCCESS( 'Successfully set configuration property.' ) )

        else:

            # no property name. Error.
            self.stdout.write( self.style.ERROR( 'You must specify a property name.' ) )

        #-- END check if property name is set --#

    #-- END overridden method handle() --#

#-- END Command class for init_config --#
