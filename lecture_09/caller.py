import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, TaskEncoder, HotelRoom


# Create queries within functions

def create_pet(name: str, species: str):
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name, origin, age, description, is_magical):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

    # artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    incomplete_tasks = TaskEncoder.objects.filter(completed=False)
    return '\n'.join(str(t) for t in incomplete_tasks)


def complete_odd_tasks():
    tasks = TaskEncoder.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    TaskEncoder.objects.filter(title=task_title).update(description=decoded_text)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.first(room_type='Deluxe')
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.room_number % 2 == 0]

    return '\n'.join(even_deluxe_rooms)