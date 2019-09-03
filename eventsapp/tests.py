from django.test import TestCase
from eventsapp.models import PublishedState, Language, Event, EventTranslation
from django.utils.timezone import make_aware
import datetime

class EmptyViewsTestCase(TestCase):

    def test_event_list_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_event_detail_status_code(self):
        response = self.client.get('/detail/')
        self.assertEquals(response.status_code, 200)

    def test_event_list_content_empty(self):
        response = self.client.get('/')
        self.assertContains(response, "<strong> Welcome, here's the list of the events: </strong>")

    def test_event_detail_content_empty(self):
        response = self.client.get('/detail/')
        self.assertContains(response, "<strong>Event not found</strong>")


    def setUp(self):
        pendingRev = PublishedState.objects.create(name='Pending review')
        published = PublishedState.objects.create(name='Published')

        spanish = Language.objects.create(name='Spanish', code='es')
        enguk = Language.objects.create(name='English (UK)', code='en_uk')
        engus = Language.objects.create(name='English (US)', code='en_us')

        date1 = datetime.datetime(2010, 1, 1, 1, 1)
        make_aware(date1)
        date2 = datetime.datetime(2011, 1, 1, 1, 1)
        make_aware(date2)
        date3 = datetime.datetime(2012, 1, 1, 1, 1)
        make_aware(date3)
        event1 = Event.objects.create(published_state=published, date=date1, author='Author1')
        event2 = Event.objects.create(published_state=published, date=date2, author='Author2')
        event3 = Event.objects.create(published_state=pendingRev, date=date3, author='Author3')

    def test_PublishedState_content(self):
        pubState = PublishedState.objects.get(pk=1)
        expected_name = f'{pubState.name}'
        self.assertEquals(expected_name, 'Pending review')

    def test_Language_content(self):
        lang = Language.objects.get(pk='es')
        expected_name = f'{lang.name}'
        expected_code = f'{lang.code}'
        self.assertEquals(expected_name, 'Spanish')
        self.assertEquals(expected_code, 'es')

    def test_Event_content(self):
        event = Event.objects.get(pk=1)
        published = PublishedState.objects.get(pk=2)
        expected_state = f'{event.published_state}'
        expected_date = f'{event.date}'
        expected_auth = f'{event.author}'
        #date = datetime.datetime(2010, 1, 1, 1, 1)
        #make_aware(date)
        self.assertEquals(expected_state, published.name)
        #self.assertEquals(expected_date, date)
        self.assertEquals(expected_auth, 'Author1')