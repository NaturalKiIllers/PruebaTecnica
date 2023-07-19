from django.db import models

class User(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)

class Context(models.Model):
    key_context = models.CharField(max_length=255, primary_key=True)
    path = models.CharField(max_length=255, null=True)
    org_id = models.CharField(max_length=255, null=True)
    key = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=255, null=True)
    agent = models.CharField(max_length=255, null=True)
    referer = models.TextField(max_length=255, null=True)
    

class Event(models.Model):
    key_event = models.CharField(max_length=255, primary_key=True)
    event_type = models.CharField(max_length=255)
    event_source = models.CharField(max_length=255)
    page = models.TextField(null=True)
    key_context = models.ForeignKey(Context, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    



