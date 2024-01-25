# import the unittest module
import unittest
# import the distance_calculator function from the module where it is defined
from distance_calculator import distance_calculator
# create a mock request object with a GET attribute
from unittest.mock import Mock
request = Mock()
request.GET = {}

# create a test class that inherits from unittest.TestCase
class TestDistanceCalculator(unittest.TestCase):
    # define a test method that starts with test_
    def test_distance_calculator(self):
        # set up some test cases with valid and invalid zipcodes
        test_cases = [
            # (zip1, zip2, expected_distance_miles)
            ('10001', '90210', 2449.3), # valid zipcodes
            ('00000', '11111', None), # invalid zipcodes
            ('abcde', 'fghij', None), # non-digit zipcodes
        ]
        # loop through the test cases
        for zip1, zip2, expected_distance_miles in test_cases:
            # set the request.GET attributes to the zipcodes
            request.GET['zip1'] = zip1
            request.GET['zip2'] = zip2
            # call the distance_calculator function with the request
            result = distance_calculator(request)
            # check if the result is a render object or a float
            if isinstance(result, float):
                # round the result to one decimal place
                result = round(result, 1)
            # assert that the result is equal to the expected distance
            self.assertEqual(result, expected_distance_miles)

# run the tests
if __name__ == '__main__':
    unittest.main()