from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import os
import sys
import re



class Command(BaseCommand):
    help = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        print "This is custom command."
        path = "./data"
        dirs = os.listdir(path)
        for file in dirs:
            print file
        genere = []
        with open("./data/movies.dat", "r") as f:
            for line in f:
                st = re.split("::", line)
                s = st[2][:-1].split("|")
                for name in s:
                    if name not in genere:
                        genere.append(name)
        print genere
