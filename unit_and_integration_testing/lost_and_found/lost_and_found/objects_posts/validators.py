from django.core.exceptions import ValidationError


def validate_max_value(max_value):
    def internal_validate(value):
        if value > max_value:
            raise ValidationError(f'{value} is greater than the max {max_value}')

    return internal_validate
