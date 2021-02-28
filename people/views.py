from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer


class PersonView(APIView):

    def get(self, request, iin):
        try:
            person = Person.objects.get(iin=iin)
        except Person.DoesNotExist:
            return Response({"description": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid() and serializer.validate(data=request.data):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_exception_handler(self):
        return self.settings.EXCEPTION_HANDLER
