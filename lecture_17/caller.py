import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer
from django.core.exceptions import ValidationError
# Create queries within functions


customer = Customer(
    name="Svetlin Nakov1",
    age=1,
    email="nakov@example",
    phone_number="+35912345678",
    website_url="htsatps://nakov.com/"
)

try:
    customer.full_clean()
    customer.save()

except ValidationError as e:
    print('\n'.join(e.messages))
