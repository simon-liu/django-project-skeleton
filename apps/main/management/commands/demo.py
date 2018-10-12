import signal

from django.core.management.base import BaseCommand

from common.log import config_logging

config_logging(filename='{{ project_name|lower }}-create-contracts.log')


class Command(BaseCommand):

    NEW_CONTRACTS_COUNT = 20

    def handle(self, *args, **options):
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        print('demo.')
