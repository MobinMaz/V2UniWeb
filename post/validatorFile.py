from django.core.exceptions import ValidationError

def validate_No_Alphabet(value):
    if any(char.isalpha() for char in value):
        raise ValidationError('در اینجا فقط میتوانید عدد وارد کنید ')
