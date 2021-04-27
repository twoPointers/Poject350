from rest_framework import serializers
from .models import Student , Result , Contact

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['reg' , 'session' , 'name' , 'credits' , 'cgpa']

class ResultSerializer(serializers.ModelSerializer):
    stuId = serializers.SerializerMethodField()

    class Meta:
        model= Result
        fields= ['stuId','courseId','courseName','semester','credit','isMajor','isLab','gpa']

    def get_stuId(self, obj):
        return obj.stuId.reg

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ['email' , 'desc']