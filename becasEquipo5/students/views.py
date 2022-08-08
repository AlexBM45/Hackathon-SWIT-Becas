from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

class StudentView(APIView):

    def get(self, request):
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentSingleView(APIView):

    def get(self, request, id):
        student = Student.objects.filter(id=id).first()
        if student is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        student = Student.objects.get(id=id)
        if student is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        if student is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        student.delete()

        return Response({'message':'Institución u Organización eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)


