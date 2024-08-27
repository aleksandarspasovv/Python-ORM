import os
import django
from datetime import date



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student
from django.db import connection
from pprint import pprint
# Run and print your queries

students = Student.objects.all()


for s in students:
    print(f'{s.first_name} {s.last_name} has email {s.email}')

pprint(Student.objects.all().query)
