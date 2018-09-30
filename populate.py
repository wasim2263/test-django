import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'test_django.settings')

django.setup()

from django_seed import Seed
seeder = Seed.seeder()


from polls.models import Question, Choice


seeder.add_entity(Question, 5)
seeder.add_entity(Choice, 10)
inserted_pks = seeder.execute()
