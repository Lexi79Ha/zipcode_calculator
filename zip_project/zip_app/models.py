from django.db import models
from pgeocode import Nominatim

class Zipcode(models.Model):
    """A model of a zipcode."""
    code = models.IntegerField(primary_key=True) # the zipcode as the primary key
    country = models.CharField(max_length=2) # the country code
    place_name = models.CharField(max_length=200) # the place name
    state = models.CharField(max_length=100) # the state name
    state_code = models.CharField(max_length=20) # the state code
    county = models.CharField(max_length=100) # the county name
    county_code = models.CharField(max_length=20) # the county code
    community = models.CharField(max_length=100) # the community name
    community_code = models.CharField(max_length=20) # the community code
    latitude = models.FloatField() # the latitude
    longitude = models.FloatField() # the longitude
    accuracy = models.IntegerField() # the accuracy

    def __str__(self):
        return f"{self.code} - {self.place_name}"

    @classmethod
    def populate_from_pgeocode(cls, country):
        """A class method to populate the model from the pgeocode module."""
        nomi = Nominatim(country) # create a Nominatim object for the country
        data = nomi.get_all_postalcodes() # get all the postalcodes for the country
        for row in data: # iterate over the rows
            zipcode = cls(**row) # create a Zipcode object from the row
            zipcode.save() # save the object to the database


# Create your models here.
