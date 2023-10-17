from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Teacher

def teacher_student_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_student_list.html', {'teachers': teachers})



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import CertificateSerializer

class CertificateVerificationView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request):
        serializer = CertificateSerializer(data=request.data)

        if serializer.is_valid():
            # Verify the certificate here
            # If verification is successful, return a success response
            return Response({"message": "Certificate verified"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
