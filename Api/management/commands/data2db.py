
from Api import serializers
from rest_framework.parsers import JSONParser
from django.core.management.base import BaseCommand, CommandError

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Paranuara.settings')
django.setup()


VEGETABLE = ['cucumber', 'beetroot', 'carrot', 'celery']


class Command(BaseCommand):
    def company2db(self, name):
        with open('./resources/'+name, 'rb') as company:
            lis_company = JSONParser().parse(company)
            serializer = serializers.CompanySerializer(
                data=lis_company, many=True)
            if serializer.is_valid():
                serializer.save()
        company.close()

    def people2db(self, name):
        with open('./resources/'+name, 'rb') as people:
            lis_people = JSONParser().parse(people)
            for el in lis_people:
                balance = filter(
                    lambda num: num in '0123456789.', el['balance'])
                el['balance'] = float(''.join(list(balance)))

                temp = el['registered']
                el['registered'] = temp.replace(' ', '')
                '''
                split food to fruits and vegatables
                '''
                el['fruits'] = ','.join(
                    [item for item in el['favouriteFood'] if item not in VEGETABLE])
                el['vegetables'] = ','.join(
                    [item for item in el['favouriteFood'] if item in VEGETABLE])
                el['friends'] = ','.join([str(item['index'])
                                          for item in el['friends']])
                el['tags'] = ','.join([str(item) for item in el['tags']])
                el.pop('favouriteFood')

            serializer = serializers.People2dbSerializer(
                data=lis_people, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        people.close()

    def handle(self, *args, **options):
        self.stdout.write('import start......')
        self.company2db('companies.json')
        self.people2db('people.json')
        self.stdout.write(self.style.SUCCESS('import done!'))


if __name__ == "__main__":
    md = Command()
