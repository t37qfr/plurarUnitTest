import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    
    #TestFixture: setUp: generate avaible elements for all test functions
    def setUp(self):
        self.phonebook = Phonebook()
        
    #TestFixture: tearDown: Run after every test function (clean up func)
    def tearDown(self):
        pass
    
        
    #Look Up
    def test_lookup_entry_by_name(self):
        self.phonebook.add('Bob','12345')
        self.assertEqual('12345',self.phonebook.lookup('Bob'))
    
    #throw a key error when missing a key
    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')
            
    #assertTrue: function return TRUE/FALSE
    #@unittest.skip("WIP")
    def test_empty_phoneboo_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        
        
    #CONSISTENT - ONE queation one test!!!
    def test_phonebook_with_normal_entries_is_consistent(self):
        #ARRANGE
        self.phonebook.add('Bob','123456')
        #ACT
        self.phonebook.add('Mary','012345')
        #ASSERT
        self.assertTrue(self.phonebook.is_consistent())
        
    @unittest.skip("WIP")
    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add('Bob','123456')
        self.phonebook.add('Mary','123456')
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add('Bob','123456')
        self.phonebook.add('Mary','123')
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add('Sue','123456')
        #assertIn: check if the elem is in an iterable
        self.assertIn('Sue',self.phonebook.get_names())
        self.assertIn('123456',self.phonebook.get_numbers())
        