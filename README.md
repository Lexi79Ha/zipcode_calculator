<h1>Zip Calculator</h1>
<h3>Zip Calculator is an app that allows users to input two valid US zipcodes and find the distance between the two zipcodes.</h3>
<h2>How does it Work?</h2>
<h4>-Zip-calculator uses Python, HTML, CSS, and Django, in order to allow the calculator to be user accessible.<br>
  -Python is used to import pgeocode to identify the "US" as the object of the database so that it pull the coordinates for all zipcodes in the United States<br>
  -The program then sets conditions that allows users to only input valid 5 digit US zipcodes.<br>- The program will produce an error message for any invalid zip codes, letters<br>
or special characters.<br>-The program then uses a distance_calculator function to pull the zip codes that users input from the HTML user interface through a get request, and uses the command "dist.quary_postal_code(zip1,zip2<br>
to calcute the distances between the two zipcodes.<br>-The pgeocode's outputs inside of kilometers, so the program converts the output into miles, before displaying to users.</h4>
<h2>What to import</h2>
<h4>-pgeocode</h4>
<h4>-django.http import Http Response</h4>
<h4>-django.shortcuts import render</h4>
<h3>Author</h3>
<h4>Alexis Harris</h4>
