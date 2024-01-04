from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from .models import message
from .serializers import Messageserializer

class MessageCreateViews(generics.CreateAPIView):
    queryset =message.objects.all()
    serializer_class =Messageserializer
    permission_classes =[permissions.IsAuthenticated]
    http_method_names=['post']
    
class MessageListView(generics.ListAPIView):
    queryset=message.objects.all()
    serializer_class=Messageserializer
    http_method_names=['get']