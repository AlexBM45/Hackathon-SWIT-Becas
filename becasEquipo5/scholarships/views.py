from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Importar modelos y serializadores a utilizar
from scholarships.models import Scholarship, Requirement
from scholarships.serializers import ScholarshipSerializer, RequirementSerializer

# # Create your views here.
class ScholarshipView(APIView):
    def get(self, request):
        scholarships = Scholarship.objects.all()
        print(scholarships)
        serializer = ScholarshipSerializer(scholarships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ScholarshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class RequirementView(APIView):
    def get(self, request):
        requirements = Requirement.objects.all()
        print(requirements)
        serializer = RequirementSerializer(requirements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RequirementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
