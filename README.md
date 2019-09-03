Event list app that displays events and their date with full translation support for these. Created using Django

The model.jpg file contains the scheme of the models

Python version=3.7.4
Django version=2.0.6

TO DO:
- Add translations for static text in both List and Detail views ("Welcome, here's the list of upcoming events:" and "Use the form below to receive updates on this event" respectively)
- Add more unit tests
- Make so that the Language selector on the List view already has selected the current Language
- Add Language selector to Detail view
- Add Name field to Event Model so they can be easily identified in django-admin
- Send the Event and EventTranslation to both List and Detail views without the need to construct and additional object that concatenates both