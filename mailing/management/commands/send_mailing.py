from django.core.management import BaseCommand

from jobs.jobs import send_mailings


class Command(BaseCommand):


    def handle(self, *args, **options):
        print('скрипт оптравки рассылок запущен')
        send_mailings()
        print('скрипт оптравки рассылок завершен')


