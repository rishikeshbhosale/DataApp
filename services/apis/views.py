from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import taluka, village, visitHistory, login
from .serializers import talukaSerializer, villageSerializer, visitHistorySerializer, loginSerializer



# Create your views here.
class loginList(APIView):
    def get(self, request):
        logins = login.objects.all()
        serializer = loginSerializer(logins, many=True)
        return Response(serializer.data)

    def post(self, request):
        logins = login.objects.all()
        serializer = loginSerializer(logins, many=True)
        return Response(serializer.data)

class talukaList(APIView):
    def get(self, request):
        talukas = taluka.objects.all()
        serializer = talukaSerializer(talukas, many=True)
        return Response(serializer.data)
    
    def post(self):
        talukas = taluka.objects.all()
        serializer =talukaSerializer(talukas, many=True)
        return Response(serializer.data)


class villageList(APIView):
    def get(self, request):
        villages = village.objects.all()
        serializer = villageSerializer(villages, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = villageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class villageEdit(APIView):
#     def get(self, request,id):
#         try:
#             villages = village.objects.get(id=id)
#         except village.DoesNotExist:
#             return Response('Village Not Found', status=status.HTTP_404_NOT_FOUND)
#         serializer =villageSerializer(villages)
#         return Response(serializer.data)
        
    
#     def put(self, request, id):
#         try:
#             villages = village.objects.get(id=id)
#         except village.DoesNotExist:
#             return Response('Village Not Found', status=status.HTTP_404_NOT_FOUND)
#         serializer = villageSerializer(villages, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class visitHistoryList(APIView):
    def get(self, request):
        visitHistorys = visitHistory.objects.all()
        serializer = visitHistorySerializer(visitHistorys, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = visitHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
