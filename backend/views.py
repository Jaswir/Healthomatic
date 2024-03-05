from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import json
import requests
import os
from .ai_utils import (
    getResponseFromChatGPT3_5Turbo,
    imagepath_to_base64,
    getResponseFromGPT4_Vision_Using_Clarifai,
    getResponseGPT4_Vision_OpenAI,
)

api_key_gpt3_5 = os.environ.get("OPEN_AI_KEY")
client = OpenAI(api_key=api_key_gpt3_5)

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
    prompt = f"I am experiencing the following symptoms: {', '.join(symptoms)}. Please provide a list of possible diseases related to these symptoms."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt}
        ]
    )
    diagnoses=response.choices[0].message.content
    return JsonResponse("{diagonoses:" + diagnoses + "}", safe=False)
    # return the response
