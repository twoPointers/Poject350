from django.db import models

# Create your models here.
class Student(models.Model):
    reg = models.CharField(max_length=15,primary_key=True)
    session = models.CharField(max_length=10)
    name= models.CharField(max_length=40)
    credits=models.DecimalField(max_digits=6 , decimal_places=2 , default= 0)
    cgpa= models.DecimalField(max_digits=5, decimal_places=2 , default = 0)
    
    def __str__(self):
        return self.reg

class Result(models.Model):
    stuId = models.ForeignKey(Student , on_delete= models.CASCADE)
    courseId= models.CharField(max_length=12)
    courseName=models.CharField(max_length=60)
    semester= models.IntegerField()
    credit= models.DecimalField(max_digits=3,decimal_places=2)
    isMajor= models.BooleanField()
    isLab= models.BooleanField()
    gpa= models.DecimalField(max_digits=3,decimal_places=2)

class Contact(models.Model):
    email= models.EmailField(max_length=254,null=True)
    desc= models.TextField()