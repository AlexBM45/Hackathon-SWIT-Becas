from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Importar modelos y serializadores a utilizar
from institutions.models import Institution,ContactPerson
from institutions.serializers import InstitutionSerializer, ContactPersonSerializer

# Create your views here.
class InstitutionView(APIView):
    #Se definen los métodos (funcionalidades)
    def get(self, request):
        institutions = Institution.objects.all()
        print(institutions)
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InstitutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)