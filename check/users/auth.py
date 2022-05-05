from .models import User
from django.db.models import Q


def authenticate(email, password):
    if email != None and password != None:
        user = User.objects.get(Q(email=email) & Q(password=password))

        return user

    return None
