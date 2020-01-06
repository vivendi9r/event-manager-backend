from django.contrib import admin
from .models import Owner, Room, Event
# Register your models here.
#
class EventAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(EventAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        return get_data

admin.site.register(Event, EventAdmin)

admin.site.register(Owner)
admin.site.register(Room)
# admin.site.register(Event)