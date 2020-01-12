
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Paranuara.settings')
django.setup()

from rest_framework.parsers import JSONParser
from Api import serializers


VEGETABLE = ['cucumber', 'beetroot', 'carrot', 'celery']

def company2db(name):
    with open('./resources/'+name,'rb') as company:
        lis_company = JSONParser().parse(company)
        serializer = serializers.CompanySerializer(data=lis_company, many=True)
        if serializer.is_valid():
            serializer.save()
    company.close()

def people2db(name):
    with open('./resources/'+name,'rb') as people:
        lis_people = JSONParser().parse(people)
        for el in lis_people:
            balance = filter(lambda num: num in '0123456789.', el['balance'])
            el['balance'] = float(''.join(list(balance)))

            temp = el['registered']
            el['registered'] = temp.replace(' ','')
            '''
            split food to fruits and vegatables
            '''
            el['fruits'] = ','.join([item for item in el['favouriteFood'] if item not in VEGETABLE])
            el['vegetables'] = ','.join([item for item in el['favouriteFood'] if item in VEGETABLE])
            el['friends'] = ','.join([str(item['index']) for item in el['friends']])
            el['tags'] = ','.join([str(item) for item in el['tags']])
            el.pop('favouriteFood')

        serializer = serializers.People2dbSerializer(data=lis_people, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    people.close()
    
if __name__ == "__main__":
    company2db('companies.json')
    people2db('people.json')

