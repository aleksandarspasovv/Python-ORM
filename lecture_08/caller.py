import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

'''
FC5204	John	Doe	15/05/1995	john.doe@university.com
FE0054	Jane	Smith	null	jane.smith@university.com
FH2014	Alice	Johnson	10/02/1998	alice.johnson@university.com
FH2015	Bob	Wilson	25/11/1996	bob.wilson@university.com

'''

# Import your models here
from main_app.models import Student


def add_students():
    student = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=date(1995, 11, 19),
        email='john.doe@university.com',
    )
    student.save()

    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com',
    )

    student = Student()
    student.student_id = 'FH2014'
    student.first_name = 'Alice'
    student.last_name = 'Johnson'
    student.birth_date = date(1998, 2, 10)
    student.email = 'alice.johnson@university.com'
    student.save()

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=date(1996, 11, 25),
        email='bob.wilson@university.com',
    )


def get_students_info():
    result = []
    all_students = Student.objects.all()
    for student in all_students:
        result.append(f'Student №. {student.student_id}: {student.first_name} {student.last_name}; {student.email}')

    return "\n".join(result)


def update_students_emails():
    all_students_emails = Student.objects.all()
    for s in all_students_emails:
        s.email = s.email.replace(s.email.split('@')[1], 'uni-students.com')
        s.save()


def truncate_students():
    all_students = Student.objects.all().delete()

