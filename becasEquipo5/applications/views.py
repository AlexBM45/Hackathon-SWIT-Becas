from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Application
from .serializers import ApplicationSerializer

class ApplicationView(APIView):

    def get(self, request):
        applications = Application.objects.all()
        print(applications)
        serializer = ApplicationSerializer(applications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationSingleView(APIView):

    def get(self, request, id):
        application = Application.objects.filter(id=id).first()
        if application is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplicationSerializer(application)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        application = Application.objects.get(id=id)
        if application is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplicationSerializer(application, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)  

    def delete(self, request, id):
        application = Application.objects.get(id=id)
        if application is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        application.delete()

        return Response({'message':'Applicación a beca eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)



