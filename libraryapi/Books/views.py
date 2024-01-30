from django.shortcuts import render
from Books.models import Book
from Books.serializers import bookserializer,userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
#mixins
# class Booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
#
#
# class Bookdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)



#generics
# class Booklist(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#
#
# class Bookdetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#


#viewset
class Bookviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = bookserializer


class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer




