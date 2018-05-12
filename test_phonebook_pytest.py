#To Run use pytest runner: python -m pytest
# No import, name file: test_.., function: test_...
# we can use the normal Python ASSERT statements

#not always has to import pytest
import pytest

from phonebook_pytest import Phonebook


#FIXTURES
@pytest.fixture
def phonebook():
    return Phonebook()


'''SKIP the test!!!'''
#@pytest.mark.skip('WIP')
def test_add_and_lookup_entry(phonebook):
    '''pytest skip the test'''
    #pytest.skip('WIP')
    phonebook.add("Bob","123")
    assert "123" == phonebook.lookup("Bob")
    
def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add('Alice','12345')
    assert 'Alice' in phonebook.names()
    assert '12345' in phonebook.numbers()
    
def test_missing_entry_raise_keyerror(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')

    