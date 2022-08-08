from django.shortcuts import get_object_or_404
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

class ScholarshipSingleView(APIView):

    def get(self, request, id):
        scholarship = Scholarship.objects.filter(id=id).first()
        if scholarship is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ScholarshipSerializer(scholarship)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        scholarship = Scholarship.objects.get(id=id)
        if scholarship is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ScholarshipSerializer(scholarship , data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        scholarship = Scholarship.objects.get(id=id)
        if scholarship is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        scholarship.delete()

        return Response({'message':'Beca eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)

#--------------------------------------------------------------------------------------------------------

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

class RequirementSingleView(APIView):

    def patch(self, request, id):
        requirements = Requirement.objects.filter(id=id).first()
        if requirements is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = RequirementSerializer(requirements, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        requirements = get_object_or_404(Requirement, id=id)
        requirements.delete()

        return Response('Requisitos eliminados', status=status.HTTP_204_NO_CONTENT)
