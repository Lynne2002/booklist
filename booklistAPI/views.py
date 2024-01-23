from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from django.http import HttpResponse

@api_view(['GET','POST'])
def books(request):
    return Response('List of the books',
                    status=status.HTTP_200_OK)

class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message':'list of orders'},200)

class BookView(APIView):
    def get(self, request, pk):
        return Response({"message": "single book with ID "+str(pk)}, status.HTTP_200_OK)
    def put(self, request,pk):
        return Response({"title:", request.data.get('title')}, status.HTTP_200_OK)