from rest_framework import serializers
from account.models import Contact

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('first_name', 'last_name', 'dob', 'address','phone_number', 'email','id',)
