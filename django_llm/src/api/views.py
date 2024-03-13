from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

import openai


# Create your views here.
openai.api_key = "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"

@api_view(["POST"])
def request_gpt(request):
    if request.method == 'POST':
        data = {'response': "test"}
        return JsonResponse(data)
    
        # Get the message from the request data
        message = request.data.get('message', '')

        # Call the OpenAI GPT API to get a response
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the generated response from the API result
        generated_response = response.choices[0].message.content

        # Create a JSON response with the generated response
        data = {'response': generated_response}
        return JsonResponse(data)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'})