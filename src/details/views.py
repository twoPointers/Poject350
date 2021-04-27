import requests
import json
from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Student , Result , Contact
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer,ResultSerializer , ContactSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


from rest_framework.views import APIView
class ContactAPI(APIView):
    def post(self, request, format=None):
        # print(request.data)
        serializer = ContactSerializer(data=request.data)
        # print('serializer' , serializer)
        if serializer.is_valid():
            serializer.save()
        return render(request,'details/success.html')

class AllResultsApi(ListAPIView):
    queryset= Result.objects.all()
    serializer_class= ResultSerializer
    filterset_fields= ['stuId','courseId','courseName','semester','credit',
    'isMajor','isLab','gpa']
    filter_backends =[DjangoFilterBackend]

class AllStudentsApi(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    filterset_fields= ['reg' , 'session' , 'name']
    filter_backends =[DjangoFilterBackend]

def myres(request):
    if request.method == 'POST':
        stuId=request.POST['stuId']
        semester=request.POST['semester']
        credit=request.POST['credit']
        isMajor=request.POST['isMajor']
        isLab=request.POST['isLab']
        results= requests.get(
            'http://localhost:8000/resultapi/',
            params= { 'stuId' : stuId ,
                    'semester' : semester,
                    'credit' : credit,
                    'isMajor' : isMajor,
                    'isLab' : isLab
                    }
        
            )

        json_results = json.loads(results.text)
        semDetail_results= {1: [],2: [],3: [],4:[],5:[],6:[],7:[],8:[]}

        semFinal_results= {
            1: {'credits': 0 ,'gpa': 0},2:{'credits': 0 ,'gpa': 0},3: {'credits': 0 ,'gpa': 0},4: {'credits': 0 ,'gpa': 0},
            5: {'credits': 0 ,'gpa': 0},6: {'credits': 0 ,'gpa': 0},7: {'credits': 0 ,'gpa': 0},8: {'credits': 0 ,'gpa': 0},
            'all': {'credits': 0 , 'gpa': 0}
        }

        for res in json_results:
            semDetail_results[res['semester']].append(res)
            if float(res['gpa']) != 0:
                semFinal_results[res['semester']]['credits'] += float(res['credit'])
                semFinal_results[res['semester']]['gpa'] +=  float(res['gpa']) * float(res['credit'])
                semFinal_results['all']['credits'] += float(res['credit'])
                semFinal_results['all']['gpa'] +=  float(res['gpa']) * float(res['credit'])


        gpa={}

        for res in semFinal_results:
            if semFinal_results[res]['credits']!=0:
                gpa[res] = round(semFinal_results[res]['gpa']/semFinal_results[res]['credits'] , 2)
        

        student= requests.get(
            'http://localhost:8000/studentapi/',
            params= { 'reg' : stuId })

        response= render(request, 'details/result.html',{ 'semdetail' : semDetail_results ,
                                                    'student' : json.loads(student.text),
                                                    'semfinal': semFinal_results,
                                                    'gpa' : gpa,
                                                    'resultLink' : results.url,
                                                    'studentLink' : student.url,
                                                    })
        return response
    else:
        raise Http404




def home(request):
    return render(request , 'details/index.html')


def sortkey(x):
    if float(x['credits']) > 83:
        return (83,float(x['cgpa']))
    else:
        return (float(x['credits']),float(x['cgpa']))

def myrank(request):
    student= requests.get('http://localhost:8000/studentapi/')
    json_student= json.loads(student.text)

    sorted_stu= sorted(json_student,
                    key= sortkey,
                    reverse=True)


    cnt=1
    for st in sorted_stu:
        st['rank']=cnt
        cnt= cnt+1

    return render(request , 'details/rank.html' , {'stu' : sorted_stu})


def createpdf(request):
    if request.method == 'POST':
        results= requests.get(request.POST['resultLink'])

        json_results = json.loads(results.text)
        semDetail_results= {1: [],2: [],3: [],4:[],5:[],6:[],7:[],8:[]}

        semFinal_results= {
            1: {'credits': 0 ,'gpa': 0},2:{'credits': 0 ,'gpa': 0},3: {'credits': 0 ,'gpa': 0},4: {'credits': 0 ,'gpa': 0},
            5: {'credits': 0 ,'gpa': 0},6: {'credits': 0 ,'gpa': 0},7: {'credits': 0 ,'gpa': 0},8: {'credits': 0 ,'gpa': 0},
            'all': {'credits': 0 , 'gpa': 0}
        }

        for res in json_results:
            semDetail_results[res['semester']].append(res)
            if float(res['gpa']) != 0:
                semFinal_results[res['semester']]['credits'] += float(res['credit'])
                semFinal_results[res['semester']]['gpa'] +=  float(res['gpa']) * float(res['credit'])
                semFinal_results['all']['credits'] += float(res['credit'])
                semFinal_results['all']['gpa'] +=  float(res['gpa']) * float(res['credit'])


        gpa={}

        for res in semFinal_results:
            if semFinal_results[res]['credits']!=0:
                gpa[res] = round(semFinal_results[res]['gpa']/semFinal_results[res]['credits'] , 2)
        

    
        student= requests.get(request.POST['studentLink'])

        template_path = 'details/pdf.html'
        context = { 'semdetail' : semDetail_results ,
                    'student' : json.loads(student.text),
                    'semfinal': semFinal_results,
                    'gpa' : gpa,
                    'resultLink' : results.url,
                    'studentLink' : student.url,
                }

        response = HttpResponse(content_type='application/pdf')
        # fname= f"{semDetail_results[0]['stuId']}.pdf"
        response['Content-Disposition'] = 'filename= "result.pdf"'
        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    else:
        raise Http404

def contactpage(request):
    return render(request, 'details/contact.html')