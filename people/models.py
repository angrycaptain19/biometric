from django.db import models
from datetime import date


class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True, blank=False, null=False)

    def age(self):
        today = date.today()
        if int(self.iin[6]) in (1, 2):
            year = 1800 + int(self.iin[:2])
        elif int(self.iin[6]) in (3, 4):
            year = 1900 + int(self.iin[:2])
        else:
            year = 2000 + int(self.iin[:2])

        born = date(year, int(self.iin[2:4]), int(self.iin[4:6]))
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return self.iin
