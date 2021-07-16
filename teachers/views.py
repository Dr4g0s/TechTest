from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from teachers.models import Teacher
from teachers import serializers
from teachers.utils import read_csv_bulk
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



last_name_param = openapi.Parameter(
    'first_letter_of_last_name', 
    openapi.IN_QUERY, 
    type=openapi.TYPE_STRING
)

subject_param = openapi.Parameter(
    'subject', 
    openapi.IN_QUERY, 
    type=openapi.TYPE_STRING
)


class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(description="Filter parameters", manual_parameters=[last_name_param, subject_param])
    def list(self, request):
        last_name = self.request.query_params.get('first_letter_of_last_name', '')
        subject = self.request.query_params.get('subject', '')
        queryset = self.queryset
        if last_name:
            queryset = queryset.filter(last_name__startswith=last_name)
        if subject:
            queryset = queryset.filter(subjects_taught__contains=subject)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'upload_bulk':
            return serializers.TeacherDataSerializer
        return self.serializer_class

    @action(detail=False, methods=['POST'], url_path='upload-bulk')
    def upload_bulk(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            read_csv_bulk(request.FILES['csv_file'].file)
            return Response(
                {'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


