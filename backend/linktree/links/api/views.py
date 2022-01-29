from turtle import st
from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from links.models import Links
from links.api.serializers import LinkSerializer

@api_view(['GET', 'POST'])
def link_list_create_api_view(request):
    
    if request.method == 'GET':
        links = Links.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
