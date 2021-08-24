from threading import Condition
from django.db import models
import datetime
from django.db.models.enums import Choices

from django.utils.regex_helper import Choice

# Create your models here.
class Teams(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image =models.ImageField(upload_to='teams/')
    address = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    twitter_link = models.URLField()
    facebook_link = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    car_title = models.CharField(max_length=30)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    year_choices = []
    for i in range(2000, (datetime.datetime.now().year+1)):
        year_choices.append((i, i))

    year = models.IntegerField(choices=year_choices)

    condition = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='cars/images/')

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    feature = models.CharField(choices=features_choices, max_length=25)
    body_style = models.CharField(max_length=20)
    engine = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    interior = models.CharField(max_length=50)
    miles  = models.IntegerField()

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    doors = models.IntegerField(choices=door_choices)
    passanger = models.IntegerField()
    vehical_no = models.CharField(max_length=30)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=30)
    no_of_owners = models.CharField(max_length=10)
    if_featured = models.BooleanField()
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True, null= True)
