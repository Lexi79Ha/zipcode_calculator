# This program is designed to calculate the distance between two zipcodes by importing pgeocode and using the dist.query_postal_code method to calculated the distance
# Conditions have been set to ensure that users can only input valid 5 digit US zipcodes
# Program will produce an error message if letters or in valid zipcodes are inputted
#Program considered any zip code outside of thew range 00501- 99950 invalid
# Geodistance automaticaaly outputs distance results in kilometers so a command has been added to converter kilometers to miles


from django.shortcuts import render # import the render function from django
from . import templates # import the templates from the current directory
from django.contrib import messages # import the messages module

# Create your views here.
def index(request): # define a view function for the index page
        context = {
                'user_authenticated': True, # set a context variable to indicate if the user is authenticated
        }
        return render(request,'first.html', context) # render the first.html template with the context

# views.py
from django.shortcuts import render # import the render function from django
from django.http import HttpResponse # import the HttpResponse class from django
import pgeocode # import the pgeocode module to calculate distances between zipcodes


dist = pgeocode.GeoDistance('US') # create a GeoDistance object for the US country code

# create a set of valid zipcodes from 00501 to 99950
valid_zipcodes = set(range(501, 99951))
def is_valid_zipcode(zipcode): # define a function to check if a zipcode is valid
    # a valid zipcode is an integer between 10000 and 99999, and also in the set of valid zipcodes
    return isinstance(zipcode, int) and 10000 <= zipcode <= 99999 and zipcode in valid_zipcodes
def distance_calculator(request): # define a function to calculate the distance between two zipcodes
    # get the zipcodes from the request
    zip1 = request.GET.get('zip1', '0') # get the first zipcode as a string, default to '0' if not provided
    zip2 = request.GET.get('zip2', '0') # get the second zipcode as a string, default to '0' if not provided

    # validate the zipcodes
    if not zip1.isdigit() or not zip2.isdigit(): # if either zipcode is not a digit
        # add an error message to the request
        messages.error(request, 'Invalid input. Please enter a 5 digit US Zipcode. Program will not accept letters or special characters.', fail_silently=True)
        # redirect to the index page
        return render(request, 'first.html')
    else: # if both zipcodes are digits
        zip1 = int(zip1) # convert them to integers
        zip2 = int(zip2)
        if not is_valid_zipcode(zip1) or not is_valid_zipcode(zip2):  # if either zipcode is invalid
            # add an error message to the request
            messages.error(request, 'Invalid input. Please enter a 5 digit US Zipcode. Program will not accept letters or special characters.', fail_silently=True)
            # redirect to the index page
            return render(request, 'first.html')
        # proceed with the rest of the code
    # calculate the distance in km
    distance = dist.query_postal_code(zip1, zip2) # use the query_postal_code method of the GeoDistance object

    # convert the distance to miles
    distance_miles = distance / 1.609 # divide the distance by 1.609 to get the equivalent in miles

    result = f'The Distance between {zip1} and {zip2} is {distance_miles:.2f} miles.' # format the result as a string with two decimal places
    context = {
        'result': result # set the result as a context variable
    }
    return render(request, 'first.html', context) # render the first.html template with the context
