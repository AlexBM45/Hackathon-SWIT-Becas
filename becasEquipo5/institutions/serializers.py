from rest_framework import serializers
from institutions.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'