#!/usr/bin/python3
"""
Unit tests for the Place model.
"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Test class for the Place model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test case to check the data type of the 'city_id' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test case to check the data type of the 'user_id' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Test case to check the data type of the 'name' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test case to check the data type of the 'description' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Test case to check the data type of the 'number_rooms' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Test case to check the data type of the 'number_bathrooms' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test case to check the data type of the 'max_guest' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Test case to check the data type of the 'price_by_night' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Test case to check the data type of the 'latitude' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test case to check the data type of the 'longitude' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """
        Test case to check the data type of the 'amenity_ids' attribute in the Place model.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

