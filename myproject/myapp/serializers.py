from rest_framework import serializers

class CertificateSerializer(serializers.Serializer):
    teacher_name = serializers.CharField()
    student_name = serializers.CharField()
    certificate_data = serializers.CharField()
