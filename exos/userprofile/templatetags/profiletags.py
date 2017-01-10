from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def bizzfuzz(profile):
    if profile.random_number % 5 == 0 and profile.random_number % 3 == 0:
        return 'BizzFuzz'
    elif profile.random_number % 5 == 0:
        return 'Fuzz'
    elif profile.random_number % 3 == 0:
        return 'Bizz'
    else:
        return profile.random_number


@register.simple_tag
def check_age(profile):
    # assuming year has 365 days, not perfect though
    if int((date.today() - profile.birthday).days/365) > 13:
        return 'allowed'
    else:
        return 'blocked'
