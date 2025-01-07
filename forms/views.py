from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form
from .utils import FieldValidator
from .serializers import FormSerializer

class FormMatcherView(APIView):
    @staticmethod
    def match_template(fields, templates):
        for template in templates:
            template_fields = template.fields
            if all(
                field in fields and FieldValidator.detect_field_type(fields[field]) == template_fields[field]
                for field in template_fields
            ):
                return template.name
        return None

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            fields = serializer.validated_data['fields']
            templates = Form.objects.all()
            match = self.match_template(fields, templates)
            if match:
                return Response({"form_name": match}, status=status.HTTP_200_OK)

            # Если совпадений нет
            field_types = {key: FieldValidator.detect_field_type(value) for key, value in fields.items()}
            return Response(field_types, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
