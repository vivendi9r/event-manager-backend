from django.contrib import admin
from .models import Owner, Room, Event
# Register your models here.

admin.site.register(Owner)
admin.site.register(Room)
admin.site.register(Event)