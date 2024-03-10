from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import openai
from openai import OpenAI
import requests
from django.db.models import Max
import json
from rest_framework.decorators import api_view


key = ""
engine = "davinci"

@api_view(["POST"])
def aa(request, story_id):
    client = OpenAI(api_key=key)
    if request.method == 'POST':
        request_json = json.loads(request.body)
        messages = request_json.get('messages', [])

        # Use OpenAI API to summarize conversation
        response = client.chat.completions.create(
             model="gpt-4",
             messages=messages,
             max_tokens=15
        )
        summary = response.choices[0].message.content if response.choices else ''

        img = client.images.generate(
            model="dall-e-3",
            prompt=summary,
            n=1,
            size="1024x1024"
        )

        img_url = img.data[0].url if img.data else ''

        # Return the first URL to the frontend
        return JsonResponse({'url': img_url})
        
    return JsonResponse({'error': 'Invalid request method'})

@api_view(["POST"])
def bb(request, story_id):
    client = OpenAI(api_key=key)
    if request.method == 'POST':
        request_json = json.loads(request.body)
        messages = request_json.get('messages', [])
        tools = [
            {
                "type": "function",
                "function": {
                "name": "fairy_tale",
                "description": "I'm going to write a fairy tale in Korean. When I write a paragraph first, you provide the next paragraph. We'll go back and forth 8 times, and then you wrap up the story.",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
                }
            }
            ]
        
        # Use OpenAI API to summarize conversation
        response = client.chat.completions.create(
             model="gpt-4",
             messages=messages,
             tools = tools,
             max_tokens=200
        )
        summary = response.choices[0].message.content if response.choices else ''

        # Return the first URL to the frontend
        return JsonResponse({'next_sentence': summary})
        
    return JsonResponse({'error': 'Invalid request method'})