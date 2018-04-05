import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"mysite.settings")

import django
# Import settings
django.setup()

import random
from myapp.models import Donor,Acceptor,Doctor
from faker import Faker

fakegen = Faker()
#topics = ['Search','Social','Marketplace','News','Games']
genders = ['M','F','O']
blood_group=['O','A','AB','B']
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def add_gender():
     t = Donor.objects.get_or_create(gender=random.choice(genders))[0]
     t.save()
     return t

def add_blood_type():
    t = Donor.objects.get_or_create(blood_group=random.choice(blood_group))[0]
    t.save()
    return t

def populatedonor(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        gen = add_gender()
        bg= add_blood_type()
        # Create Fake Data for entry
        #fake_ = fakegen.url()
        fake_dob = fakegen.date()
        fake_name = fakegen.name()
        fake_phone= fakegen.phone_number()

        # Create new Webpage Entry
        #webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        d1=Donor.objects.get_or_create(name=fake_name,dob=fake_date,blood_group=bg,gender=gen,phone=fake_phone)[0]
        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        #accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

def populateacceptor(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        gen = add_gender()
        bg= add_blood_type()
        # Create Fake Data for entry
        #fake_ = fakegen.url()
        fake_dob = fakegen.date()
        fake_name = fakegen.name()
        fake_phone= fakegen.phone_number()

        # Create new Webpage Entry
        #webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        d1=Acceptor.objects.get_or_create(name=fake_name,dob=fake_date,blood_group=bg,gender=gen,phone=fake_phone)[0]
        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        #accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populatedonor(20)
    populateacceptor(20)
    print('Populating Complete')
