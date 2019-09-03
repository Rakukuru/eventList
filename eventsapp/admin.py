from django.contrib import admin
from .models import PublishedState, Language, Event, EventTranslation, EventSubscription

admin.site.register(PublishedState)
admin.site.register(Language)
admin.site.register(Event)
admin.site.register(EventTranslation)
admin.site.register(EventSubscription)
