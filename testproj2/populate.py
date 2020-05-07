import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproj.settings')

import django
django.setup()


import random
from testapp.models import *
from faker import Faker

fakegen = Faker()

topics = ['search', 'social', 'marketplace', 'news', 'games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        wbpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=wbpg, date=fake_date)[0]

if __name__ == '__main__':
    print('Poulating database')
    populate(26)
    print('populating complete')
