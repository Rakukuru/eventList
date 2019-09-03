from django.db import models
#from django.utils import timezone


class PublishedState(models.Model):
    name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)    # Name to identify the language on django admin. Ex: "Spanish"
    code = models.CharField(max_length=50, primary_key=True)    # Code that identifies the language, used to to access variables. Ex: "es"

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Event(models.Model):
    published_state = models.ForeignKey('PublishedState', on_delete=models.CASCADE)
    date = models.DateTimeField(
            blank=True, null=True)
    author = models.CharField(max_length=50)

    def publish(self):
        self.save()


class EventTranslation(models.Model):
    eventOriginal = models.ForeignKey('Event', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
    	# Association unique so no Translations for the same Language can be created for the same Event.
        unique_together = (("eventOriginal", "language"),)    

    def publish(self):
        self.save()

    def __str__(self):
    	return self.eventName


class EventSubscription(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)

    def publish(self):
        self.save()

    def __str__(self):
    	return self.name

