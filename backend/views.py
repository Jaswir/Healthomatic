from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import requests
import os

@api_view(['GET'])
def getPriorityFromSymptoms(request, symptoms):
    
    #TODO call the model to get the priority from the symptoms
    
   return JsonResponse("{priority: 'emergency'}", safe=False)
                            

@api_view(['GET'])
def getSymptomsFromImage(request, image):

     #TODO call the model to get symptoms from the image
    
    # return the response
    return JsonResponse("{symptoms: ['cough', 'fever', 'headache']}",  safe=False)


@api_view(['GET'])
def getDiagnosesFromSymptoms(request, symptoms):

    #TODO call the model to get the diagnoses

    # return the response
    return JsonResponse("{diagnoses: ['flu', 'cold']}", safe=False)