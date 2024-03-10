from django.shortcuts import render
from rest_framework.response import Response
import os
import boto3
import json
from collections import deque
from rest_framework.decorators import api_view

messages = deque([])
# messages = deque([{"role": "user", "content": "hello there"}, {"role": "bot", "content": "no"}])

# Create your views here.
@api_view(["POST"])
def chat(request, story_id):
    if request.method == "POST":
       #user = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]).user
        try:
            print(request)
            request_json = json.loads(request.body)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=400)
        
        # 요청 변환을 수행합니다.
        request_next_sentence = claude(request)
        trequest_summary = "stylized picture of a cute old steampunk robot" #transform_summary(request_json)
        return Response({"next_sentence": request_next_sentence})
    

def combine(messages):
    chatlog = ""
    for message in messages:
        chatlog += f"\nRole:{message['role']}"
        chatlog += f"\n{message['content']}\n"
    return chatlog


def claude(request):
    client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1024,
                "messages": request.get("messages"),
                "system": """너는 내 국어 선생님이야, 반말을 쓰도록해해. 나는 2페이지 동화를 쓸 생각인데 brainstorming에 도움을줘. 내가 한 단락쓰면 너도 한 단락써서 이야기를 재밌게 할꺼야.
추가적으로 내차례는 따로 말을 할 필요는 없어.""",
            }
        ),
    )
    # Process and print the response(s)
    response_body = json.loads(response.get("body").read())
    for output in response_body.get("content", []):
        print(output["text"])
        messages.appendleft({"role": "bot", "content": output})
        return output["text"]
    

