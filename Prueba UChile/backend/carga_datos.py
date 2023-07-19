
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from django.db import models
from datosUCH.models import User, Context, Event


from django.db import IntegrityError
from django.utils.dateparse import parse_datetime

import json

from django.utils import timezone
from datetime import datetime

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
    #Eliminar todos los usuarios
    User.objects.all().delete()
    Context.objects.all().delete()
    Event.objects.all().delete()


# # Obtener los pares clave-valor de user_id y clave
user_data = []
context_data=[]

for key, value in data['context'].items():
    if 'user_id' in value:
        user_id = value['user_id']
        username = data['username'].get(key, "")
        user_data.append((key, user_id, username))

# Crear y guardar instancias del modelo User
for key, user_id, username in user_data:
    if not user_id:
        user_id = ""

    user = User(key=key,user_id=user_id, username=username)
    user.save()

    # Imprimir el usuario recién creado
    print("Nuevo usuario creado:")
    print("ID:", user.key)
    print("user_id:", user.user_id)
    print("username:", user.username)
    print("---")

#Obtener los datos de context
user_data = []
context_data = []

for key, value in data['context'].items():
    if 'path' in value and 'org_id' in value and 'course_id' in value:
        path = value.get('path')
        org_id = value.get('org_id')
        course_id = value.get('course_id')
        agent = data['agent'].get(key)
        referer = data['referer'].get(key)
        user_key =key
        try:
            user = User.objects.get(key=user_key)
        except User.DoesNotExist:
            user = None

            # Guardar la instancia de Context
        context = Context(key_context=key,path=path, org_id=org_id, key=user, course_id=course_id,agent=agent,referer=referer)
        context.save()

            # Imprimir el contexto recién creado
        print("Nuevo contexto creado:")
        print("ID:", context.key_context)
        print("key:", context.key)
        print("path:", context.path)
        print("org_id:", context.org_id)
        print("course_id:", context.course_id)
        print("agent:", context.agent)
        print("referer:", context.referer)
        print("---")
        if user:
            print("Usuario relacionado:")
            print("key:", user.key)
            print("user_id:", user.user_id)
            print("username:", user.username)
        print("---")






user_data = []
context_data = []

for key, value in data['event_type'].items():
    key_event = key
    event_type = value.replace('/', '-')
    event_source = data["event_source"].get(key, None)
    
    page = data["page"].get(key,None)
    timestamp_str = data['time'].get(key)
    fecha_dt = datetime.fromisoformat(timestamp_str)
    fecha_date = fecha_dt.date()
    fecha_time = fecha_dt.time().replace(second=0,microsecond=0)
 


    key_context = key
    try:
        context = Context.objects.get(key_context=key_context)
    except Context.DoesNotExist:
        continue
        # Guardar la instancia de Context
    event = Event(key_event=key,event_type=event_type, event_source=event_source, page=page, key_context=context,fecha=fecha_date, hora=fecha_time)
    event.save()
    # Imprimir el contexto recién creado
    print("Nuevo contexto creado:")
    print(key)
    print("id:", event.key_event)
    print("type:", event.event_type)
    print("source:", event.event_source)
    print("page:", event.page)
    print("context:", event.key_context)
    print("FECHA:", event.fecha)
    print("HORA:", event.hora)



       