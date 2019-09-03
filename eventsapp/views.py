from django.shortcuts import render, redirect
from django.views import generic
from .models import Event
from .models import EventTranslation
from .forms import LanguageForm, EventSubscriptionForm

class EventList(generic.ListView):
    model = Event 
    context_object_name = "filteredList"   # name of the list as a template variable
    template_name  = 'eventlist.html'    # template location

    def get_queryset(self):
    	filteredLanguage = self.request.GET.get('language', 'en_uk')
    	return Event.objects.filter(published_state__name__contains = 'Published', eventtranslation__language__code__contains=filteredLanguage)

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        filteredLanguage = self.request.GET.get('language', 'en_uk')
        eventList = Event.objects.filter(published_state__name__contains = 'Published', eventtranslation__language__code__contains=filteredLanguage)

        events = []

        for event in eventList:
        	trans = EventTranslation.objects.filter(eventOriginal__id__contains=event.id, language__code__contains=filteredLanguage).first()

        	events.append({
        		'id': event.id,
        		'date': event.date,
        		'name': trans.eventName,
        		})

        context['events'] = events
        context['form'] = LanguageForm()
        context['language'] = filteredLanguage
        return context


class EventDetail(generic.ListView):
    model = Event 
    context_object_name = "eventDetail"   # name of the list as a template variable
    template_name  = 'eventdetail.html'    # template location

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        eventId = self.request.GET.get('event', 0)
        filteredLanguage = self.request.GET.get('language', 'en_uk')

        if(eventId!=None):
        	event = Event.objects.filter(published_state__name__contains = 'Published', eventtranslation__language__code__contains=filteredLanguage, id = eventId).first()
        	if(event!=None): 
	        	trans = EventTranslation.objects.filter(eventOriginal__id__contains=eventId, language__code__contains=filteredLanguage).first()

	        	eventInfo = {
	        		'id': event.id,
	        		'date': event.date,
	        		'name': trans.eventName,
	        		'description': trans.description
	        	}

	        	context['eventInfo'] = eventInfo
	        	context['form'] = EventSubscriptionForm()
	        else:
	        	# If the event could not be found, send an error message on screen
        		context['eventInfo'] = { 'name': "Event not found" }
        return context

# POST Request Handlers
def changeLanguage(request):
    if request.method == "POST":
        form = EventSubscriptionForm(request.POST)
        language = request.POST.get('language', 'en_uk')
        return redirect('/?language='+language)
    else:
        return render(request, '/', {'form': form})

def postSubscription(request):
    if request.method == "POST":
        form = EventSubscriptionForm(request.POST)
        eventId = request.POST.get('event', '')
        if form.is_valid():
           bbb = form.save(commit=False)
           bbb.event_id = Event.objects.get(pk=eventId)
           bbb.save()
           return redirect('events')
    else:
        return render(request, '/', {'form': form})





