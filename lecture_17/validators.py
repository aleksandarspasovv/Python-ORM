from django.core.exceptions import ValidationError


class ValidateName:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.ValidateName',
            (self.message,),
            {}
        )


class ValidatePhoneNumber:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if not value.startswith('+359') or len(value) != 13 or not value[4:].isdigit():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.ValidatePhoneNumber',
            (self.message,),
            {}
        )
