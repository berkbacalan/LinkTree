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


@api_view(['GET', 'PUT', 'DELETE'])
def link_detail_api_view(request, pk):
    try:
        link_instance = Links.objects.get(pk=pk)
    except Links.DoesNotExist:
        return Response({
            'errors': {
                'code': 404,
                'message': 'There is no link with ({pk}) in link tree.'
            }
        },
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LinkSerializer(link_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LinkSerializer(link_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        link_instance.delete()
        return Response({
            'Action': {
                'code': 204,
                'message': 'Link has deleted with id ({pk}) from link tree.'
            }
        }, status=status.HTTP_204_NO_CONTENT)
