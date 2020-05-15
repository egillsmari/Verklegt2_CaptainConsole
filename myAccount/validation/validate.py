from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validateCardNumber(number):
    if len(str(number)) != 16:
        raise ValidationError(
        'Card number must contain 16 numbers'
        )


def validateCVV(number):
    if len(str(number)) != 3:
        raise ValidationError(
        'CVV number must contain 16 numbers'
        )
