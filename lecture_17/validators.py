from django.core.exceptions import ValidationError


class ValidateName:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)


class ValidatePhoneNumber:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        lef_side = value[:4]
        right_side = value[4:]
        if not lef_side == '+359' and len(right_side) == 9:
            raise ValidationError(self.message)
