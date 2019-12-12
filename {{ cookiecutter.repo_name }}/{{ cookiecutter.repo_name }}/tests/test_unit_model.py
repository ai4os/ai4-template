# -*- coding: utf-8 -*-
import unittest
import {{ cookiecutter.repo_name }}.models.deep_api as deep_api

class TestModelMethods(unittest.TestCase):
    
    def setUp(self):
        self.meta = deep_api.get_metadata()
        
    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)
        
    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['Name'].replace('-','_'),
                        '{{ cookiecutter.repo_name }}'.replace('-','_'))
        self.assertEqual(self.meta['Author'], '{{ cookiecutter.author_name }}')
        self.assertEqual(self.meta['Author-email'], '{{ cookiecutter.author_email }}')


if __name__ == '__main__':
    unittest.main()
