from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=254)
    #Ideally use a library to validate address and phone number form\
    #address lib: https://github.com/furious-luke/django-address
    #phone lib: https://github.com/stefanfoulis/django-phonenumber-field
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        name = f'{self.last_name}, {self.first_name}'
        return name
