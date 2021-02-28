from rest_framework import serializers
from .models import Person
from datetime import date


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('iin', 'age')

    def validate(self, data):
        iin = data['iin']
        if not isinstance(iin, str):
            raise serializers.ValidationError("IIN has to be provided as string!")

        if not iin.isdecimal():
            raise serializers.ValidationError("IIN has to contain only numbers!")

        if len(iin) != 12:
            raise serializers.ValidationError("The length of IIN has to be exactly 12 symbols!")

        if iin == iin[0] * 12:
            raise serializers.ValidationError("IIN can not contain 12 identical symbols!")

        if int(iin[6]) < 1 or int(iin[6]) > 6:
            raise serializers.ValidationError('Seventh symbol has to be in range from 1 to 6')

        if int(iin[6]) in (1, 2):
            year = 1800 + int(iin[:2])
        elif int(iin[6]) in (3, 4):
            year = 1900 + int(iin[:2])
        else:
            year = 2000 + int(iin[:2])

        month = int(iin[2:4])
        day = int(iin[4:6])

        try:
            date(year, month, day)
        except Exception as ex:
            raise serializers.ValidationError("Not valid date in the IIN provided!")

        return super(PersonSerializer, self).validate(data)
