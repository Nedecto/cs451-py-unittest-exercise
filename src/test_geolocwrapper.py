# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper

class TestGeoLocWrapper(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """
    def test_init(self):
        """Unit test for GeoLocWrapper constructor."""
        a = GeoLocWrapper('1314 chavez st, las vegas, nm')  # remove this and write the test for the constructor.

    # Begin adding your unit tests for the GeoLocWrapper module.
    def test_get_distance_miles(self):
        a = GeoLocWrapper('1314 chavez st, las vegas, nm')        
        dist = a.get_distance_miles('1701 bryant st, denver, co')
        self.assertEqual(dist, 286.80227495947776)
    def test_get_distance_kilometers(self):
        a = GeoLocWrapper('1314 chavez st, las vegas, nm')        
        dist = a.get_distance_kilometers('1701 bryant st, denver, co')
        self.assertEqual(dist, 461.5635203923858)
if __name__ == '__main__':
    unittest.main()