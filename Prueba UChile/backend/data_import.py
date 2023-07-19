
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

with open('data.json', encoding='utf-8') as file:
    json_data = json.load(file)
    # Eliminar todos los usuarios
    User.objects.all().delete()

 # Obtener los valores de user_id
user_ids = [value['user_id'] for value in data['context'].values() if 'user_id' in value]

# Imprimir los valores obtenidos
print("user_ids:", user_ids)                