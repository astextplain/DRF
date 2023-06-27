from django.shortcuts import render
from .models import Student
from .serializers import Studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        model = Student.objects.get(id=pk)
    # print(model)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':

        serializer = Studentserializers(model)
    # print(serializer)
    # print(serializer.data)
    # jason_data = JSONRenderer().render(serializer.data)
    # print(jason_data)
    # return HttpResponse(jason_data, content_type='application/json')
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Studentserializers(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        model = Student.objects.all()
        serializer = Studentserializers(model, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
