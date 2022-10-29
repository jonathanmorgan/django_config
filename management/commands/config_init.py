from django.core.management.base import BaseCommand, CommandError
from django_config.models import Config_Property

class Command( BaseCommand ):

    help = 'Initializes standard configuration properties for django_event_logging'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):

        # call the initialization method.
        Config_Property.initialize_properties()

        self.stdout.write( self.style.SUCCESS( 'Successfully initialized configuration.' ) )

    #-- END overridden method handle() --#

#-- END Command class for init_config --#
