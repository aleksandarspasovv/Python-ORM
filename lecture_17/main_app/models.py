from django.core.validators import MinLengthValidator
from django.db import models

from validators import ValidateName, ValidateAge


# Create your models here.


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[ValidateName('Name can only contain letters and spaces')]
    )
    age = models.PositiveIntegerField(
        validators=MinLengthValidator(18, message='Age must be greater than or equal to 18')
    )
    email = models.EmailField()