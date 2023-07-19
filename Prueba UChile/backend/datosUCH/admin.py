from django.contrib import admin
from .models import Context, User, Event

# Register your models here.
admin.site.register(Context)
admin.site.register(User)
admin.site.register(Event)
