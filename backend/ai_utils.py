import os
import base64

from openai import OpenAI
from clarifai.client.model import Model
from clarifai.client.input import Inputs

# Set your OpenAI API key
api_key = os.environ.get("OPEN_AI_KEY")
client = OpenAI(api_key=api_key)

# Set your Clarifai API key
os.environ["CLARIFAI_PAT"] = os.environ.get("CLARIFAI_PAT")

print("setup AI ")


def getResponseFromChatGPT3_5Turbo(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output JSON.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def imagepath_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def getResponseFromGPT4_Vision_Using_Clarifai(prompt, base64_image):
    inference_params = dict(temperature=0.2, max_tokens=2048, image_base64=base64_image)

    # Model Predict
    model_prediction = Model(
        "https://clarifai.com/openai/chat-completion/models/gpt-4-vision"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    return model_prediction.outputs[0].data.text.raw



#Example usage:
#image_path = 'Dysgraphia.jpg'
#prompt = "What does the text in this image say?"
#image64 = imagepath_to_base64(image_path)
#print(getResponseFromGPT4_Vision_Using_Clarifai(prompt, image64))