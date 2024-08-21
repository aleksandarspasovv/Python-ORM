import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, Avg, Sum, F


# Create queries within functions
def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    if not astronauts.exists():
        return ""

    result = []
    for astronaut in astronauts:
        status = "Active" if astronaut.is_active else "Inactive"
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}")
    return "\n".join(result)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.annotate(mission_count=Count('mission')).order_by('-mission_count',

                                                                                        'phone_number').first()
    if not top_astronaut or top_astronaut.mission_count == 0:
        return "No data."
    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_count} missions."


def get_top_commander():
    top_commander = Astronaut.objects.annotate(commander_count=Count('missions_commander')).order_by('-commander_count',
                                                                                                     'phone_number').first()
    if not top_commander or top_commander.commander_count == 0:
        return "No data."
    return f"Top Commander: {top_commander.name} with {top_commander.commander_count} commanded missions."


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else "TBA"

    astronauts = last_completed_mission.astronauts.order_by('name')
    astronaut_names = ", ".join([astronaut.name for astronaut in astronauts])
    total_spacewalks = astronauts.aggregate(total=Sum('spacewalks'))['total']

    total_spacewalks = total_spacewalks if total_spacewalks else 0

    return (f"The last completed mission is: {last_completed_mission.name}. Commander: {commander_name}. "
            f"Astronauts: {astronaut_names}. Spacecraft: {last_completed_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    most_used_spacecraft = Spacecraft.objects.annotate(mission_count=Count('mission')).order_by('-mission_count',
                                                                                                'name').first()
    if not most_used_spacecraft or most_used_spacecraft.mission_count == 0:
        return "No data."

    num_astronauts = Astronaut.objects.filter(mission__spacecraft=most_used_spacecraft).distinct().count()
    return (
        f"The most used spacecraft is: {most_used_spacecraft.name}, manufactured by {most_used_spacecraft.manufacturer}, "
        f"used in {most_used_spacecraft.mission_count} missions, astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    if not spacecrafts.exists():
        return "No changes in weight."


    num_of_spacecrafts_affected = spacecrafts.count()
    spacecrafts.update(weight=F('weight') - 200.0)

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    avg_weight = round(avg_weight, 1)

    return (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight}kg")
