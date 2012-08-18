# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, username, **option):
        User.objects.filter(username=username).update(is_staff=True, is_superuser=True)
