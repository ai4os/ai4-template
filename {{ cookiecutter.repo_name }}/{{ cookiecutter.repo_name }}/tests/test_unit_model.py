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
        self.assertEqual(self.meta['name'].replace('-','_'),
                        '{{ cookiecutter.repo_name }}'.lower().replace('-','_'))
        self.assertEqual(self.meta['author'],
                         '{{ cookiecutter.author_name }}'.lower())
        self.assertEqual(self.meta['author-email'],
                         '{{ cookiecutter.author_email }}'.lower())
        self.assertEqual(self.meta['license'], 
                         '{{ cookiecutter.open_source_license }}'.lower())


if __name__ == '__main__':
    unittest.main()
