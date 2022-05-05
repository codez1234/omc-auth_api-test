from django.db import models

# importing validationerror
from django.core.exceptions import ValidationError


'''
for creating  --> 

name
email
phone_number
password
confirm password / password2
'''


def validate_password(value):
    if len(value) <= 3:
        raise ValidationError(('%(value)s should be greater than 3 '),
                              params={'value': value},
                              )


class User(models.Model):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )

    phone_number = models.IntegerField(
        verbose_name='Phone_Number',
        unique=True,
    )

    password = models.CharField(max_length=50, validators=[validate_password])

    name = models.CharField(max_length=200)
    is_omc = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

# Now just before we save the object, we ask django to validate it by calling the full_clean() method.

# model_name.full_clean()
# model_name.save()
