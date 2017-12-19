from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Contact
from account.serializer import ContactSerializer

# Create your views here.

@api_view(['GET','PUT','DELETE'])
def contact(request, slug):
    try:
        contact = Contact.objects.get(id=slug)
    except Contact.DoesNotExist:
        return Response("status=status.HTTP_404_NOT_FOUND")

    if request.method =='GET':
      contacts = Contact.objects.filter(id=slug)
      serializer = ContactSerializer(contacts, many=True)
      return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

    elif request.method =='DELETE':
        contact.delete()
        return Response('contact delete')

@api_view(['GET','POST'])
def contact_list(request):
    if request.method =='POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    elif request.method=='GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
