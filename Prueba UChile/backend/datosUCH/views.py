from rest_framework import generics
from .models import User, Context, Event 
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, ContextSerializer, EventSerializer
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.db.models.functions import ExtractHour, ExtractMinute
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.db.models import Q

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20  # Mostrar 20 elementos por página
    pagination_class.page_query_param = 'page'  # Nombre del parámetro de consulta para especificar el número de página

class ContextList(generics.ListCreateAPIView):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20  # Mostrar 20 elementos por página
    pagination_class.page_query_param = 'page'  # Nombre del parámetro de consulta para especificar el número de página

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20  # Mostrar 20 elementos por página
    pagination_class.page_query_param = 'page'  # Nombre del parámetro de consulta para especificar el número de página

from rest_framework import status
from datetime import datetime

import os
from django.http import HttpResponse
class EventFilterViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20  # Establece el tamaño de página deseado
    queryset = User.objects.all()
    def list(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        event_type = request.query_params.get('event_type')
        event_source = request.query_params.get('event_source')
        course_id = request.query_params.get('course_id')
        fecha = request.query_params.get('fecha')
        hora = request.query_params.get('hora')
        queryset = Event.objects.all()
        if username:
            users = User.objects.filter(username=username)
            if users.exists():
                context_data = Context.objects.filter(key__in=users)
                queryset = queryset.filter(key_context__in=context_data)
        if event_type:
            queryset = queryset.filter(event_type=event_type)

        if event_source:
            queryset = queryset.filter(event_source=event_source)
        if course_id:
            course_id=course_id.replace(" ","+")
            course = Context.objects.filter(course_id=course_id)
            key_contexts = course.values_list('key_context', flat=True)
            queryset = queryset.filter(key_context__in=key_contexts)
        if fecha:
            queryset = queryset.filter(fecha=fecha)


        if hora:
            queryset = queryset.filter(hora=hora)


        event_serializer = EventSerializer(queryset, many=True)


        data = {
            'events': event_serializer.data,
        }
        return Response(data)

