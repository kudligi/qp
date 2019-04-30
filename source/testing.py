import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_metadata_1(self):
        res = requests.get('http://0.0.0.0:5000/metadata/course_list')
        self.assertEqual(res.text, '["UG"]\n'  )

    def test_metadata_2(self):
        res = requests.get('http://0.0.0.0:5000/metadata/departments_list/UG')
        self.assertEqual(res.text, '["forensic_medicine","community_medicine_2","community_medicine_1","ent"]\n')



unittest.main()