from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view
import json
import logging

logger=logging.getLogger('django')

from .models import Post
@api_view(['GET'])
def add_post(request):
    title=request.GET.get('title','')
    content=request.GET.get('content','')
    photo=request.GET.get('photo','')
    author=request.GET.get('author','')

    new_post =Post()
    new_post.title=title
    new_post.content=content
    new_post.photo=photo
    new_post.author=author
    new_post.save()
    logger.debug("******* myhello_api"+title)
    if title:
        return Response({'data':title},status=status.HTTP_200_OK)
    else:
        return  Response(
            {'res':'xxx'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def list_post(request):
    index =request.GET.get('index',None)
    if index:
        posts=Post.objects.filter(id=index).values()
    else:
        posts=Post.objects.all().values()
    return JsonResponse(list(posts),safe=False)

@api_view(['GET'])
def delete_post(request):
    index =request.GET.get('index',None)
    result = Post.objects.filter(id=index).delete()
    if result:
        return Response({'data':result},status=status.HTTP_200_OK)
    else:
        return  Response(
            {'res':'fail to delete'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def myhello_api(request):
    my_name =request.GET.get('name',None)
    if my_name:
        return Response({'data':'hello'+my_name},status=status.HTTP_200_OK)
    else:
        return Response(
            {'res':'xxx'},status=status.HTTP_400_BAD_REQUEST)
#def myIndex(request):
#    my_name = request.GET.get('name','CGU')
#    return HttpResponse('Hello'+my_name)


