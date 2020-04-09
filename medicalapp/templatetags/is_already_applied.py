from django import template

from django.contrib.auth.models import Group
from ..models import MedicalHistory

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.simple_tag(name='is_already_applied')
def is_already_applied(user):
    applied = MedicalHistory.objects.filter(user=user)
    if applied:
        return True
    else:
        return False
