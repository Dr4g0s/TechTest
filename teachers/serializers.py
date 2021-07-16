from rest_framework import serializers
from teachers.models import Teacher, TeacherData



class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('id',)


class TeacherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherData
        fields = ('id', 'csv_file')
        read_only_fields = ('id',)