from rest_framework import serializers
from main import models
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields='__all__'

