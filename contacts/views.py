from django.shortcuts import render_to_response
from contacts.models import Bio

def view_contact(request):
    bio_list = Bio.objects.all().order_by('name')
    return render_to_response('../templates/base.html', {'bio_list': bio_list})
