from django.db import models

class Contacts(models.Model):
    email = models.EmailField()
    jid = models.EmailField()
    skype = models.CharField(max_length=50)
    other = models.TextField()

class Bio(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField('Date birth')
    about = models.TextField()
    contacts = models.ForeignKey(Contacts)

    def __unicode__(self):
        return self.name