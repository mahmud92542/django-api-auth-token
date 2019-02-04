from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.views import status
from .models import *
from .serializers import *

class FriendsViewset(ListAPIView): 
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()


class FriendViewset(CreateAPIView): #CreateApiView, django will handle CRUD
	serializer_class = FriendSerializer
	query_set = Friend.objects.all() #query_set is for create


class BelongingViewset(ListAPIView):
	serializer_class = BelongingSerializer
	queryset = Belonging.objects.all() #queryset is for list (list means get)

class BelongViewset(CreateAPIView):
	serializer_class = BelongingSerializer
	query_set = Belonging.objects.all()

class BorrowedViewset(APIView):
	def get(self,request):
		borrowList = Borrowed.objects.all()
		serializer = BorrowedSerializer(borrowList, many=True)
		return Response (serializer.data)


'''class BorrowUpdate(UpdateAPIView):
	serializer_class = BorrowedSerializer
	queryset = Borrowed.objects.all()'''

class BorrowViewset(CreateAPIView):
	serializer_class = BorrowedSerializer
	queryset = Borrowed.objects.all()
