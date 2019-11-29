
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
def validate_email(value):
    if not "gmail.com" in value:
        raise ValidationError("sorry, this is not a valid email")
    return value
