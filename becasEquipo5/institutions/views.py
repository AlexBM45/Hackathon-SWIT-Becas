from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ContactPerson, Institution
from .serializers import ContactPersonSerializer, InstitutionSerializer, InstitutionContactSerializer

class InstitutionView(APIView):

    def get(self, request):
        institutions = Institution.objects.all()
        print(institutions)
        serializer = InstitutionSerializer(institutions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = InstitutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class InstitutionSingleView(APIView):

    def get(self, request, id):
        institution = Institution.objects.filter(id=id).first()
        if institution is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = InstitutionSerializer(institution)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        institution = Institution.objects.get(id=id)
        if institution is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = InstitutionSerializer(institution, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        institution = Institution.objects.get(id=id)
        if institution is None:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        institution.delete()

        return Response({'message':'Institución u Organización eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)


class ContactView(APIView):

    def get(self, request):
        contacts = ContactPerson.objects.all()
        print(contacts)
        serializer = ContactPersonSerializer(contacts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactPersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactSingleView(APIView):

    def patch(self, request, id):
        contact = ContactPerson.objects.filter(id=id).first()
        if contact is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactPersonSerializer(contact, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        contact = get_object_or_404(ContactPerson, id=id)
        contact.delete()

        return Response('Contacto eliminado', status=status.HTTP_204_NO_CONTENT)