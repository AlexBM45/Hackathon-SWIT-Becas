from rest_framework import serializers
from .models import Institution, ContactPerson

class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


def to_representation(self, instance):
    return {
        'id': instance.id,
        'institution': instance.institution.name,
        'email': instance.email
    }


class InstitutionContactSerializer(serializers.ModelSerializer):
    
    contact = serializers.SerializerMethodField()

    class Meta:
        model = Institution
        fields = '__all__'

    def get_contact(self, obj):
        selected_contact = ContactPerson.objects.filter(institution__id=obj.id)
        return InstitutionContactSerializer(selected_contact, many=True).data