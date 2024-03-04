from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import requests
import os
from .ai_utils import (
    getResponseFromChatGPT3_5Turbo,
    imagepath_to_base64,
    getResponseFromGPT4_Vision_Using_Clarifai,
    getResponseGPT4_Vision_OpenAI,
)


@api_view(["GET"])
def getPriorityFromSymptoms(request, symptoms):

    # TODO call the model to get the priority from the symptoms

    return JsonResponse("{priority: 'emergency'}", safe=False)


@api_view(["GET"])
def getSymptomsFromImage(request, image):

    # TODO call the model to get symptoms from the image
    image_path = "Dysgraphia.jpg"
    prompt = "What does the text in this image say?"
    base64_image = imagepath_to_base64(image_path)

    symptoms = getResponseFromGPT4_Vision_Using_Clarifai(prompt, base64_image)

    # return the response
    return JsonResponse("{symptoms:" + symptoms + "}", safe=False)


@api_view(["GET"])
def getDiagnosesFromSymptoms(request, symptoms):

    # TODO call the model to get the diagnoses from the symptoms

    # return the response
    return JsonResponse("{diagnoses: ['flu', 'cold']}", safe=False)
