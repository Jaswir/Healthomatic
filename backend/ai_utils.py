import os
import base64
import requests


from openai import OpenAI
from clarifai.client.model import Model
from clarifai.client.input import Inputs

# Set your OpenAI API key
api_key_gpt3_5 = os.environ.get("OPEN_AI_KEY")
api_key_gpt4_0 = os.environ.get("OPEN_AI_KEY_GPT4")
client = OpenAI(api_key=api_key_gpt3_5)

# Set your Clarifai API key
#os.environ["CLARIFAI_PAT"] = os.environ.get("CLARIFAI_PAT")

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


def getResponseGPT4_Vision_OpenAI(prompt, base64_image):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key_gpt4_0}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 2048,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    return response.json()['choices'][0]['message']['content']


