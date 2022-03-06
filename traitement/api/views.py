from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from traitement.models import Question
from .serializers import QuestionSerializers


@api_view(['GET'])
def vote(request):
    question = Question.objects.all()
    fullstack = Question.objects.filter(reponse='fullstack').count()
    backend = Question.objects.filter(reponse='backend').count()
    frontend = Question.objects.filter(reponse='frontend').count()
    
    context = {
        'fullstack':fullstack,
        'backend':backend,
        'frontend':frontend
    }
    #serializer = QuestionSerializers(question, many=True)
    return Response(context)