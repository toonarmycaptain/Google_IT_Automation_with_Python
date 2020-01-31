import pytest

from Using_Python_to_Interact_with_the_Operating_System.regex_examples import (check_character_groups,
                                                                               check_sentence,
                                                                               check_time,
                                                                               check_web_address,
                                                                               check_zip_code,
                                                                               convert_phone_number,
                                                                               long_words,
                                                                               rearrange_name,
                                                                               )


@pytest.mark.parametrize(
    'test_string, check_result',
    [("The zip codes for New York are 10001 thru 11104.", True),
     ("90210 is a TV show", False),
     ("1234 is not a zip code and neither is 5678 or 9101-11213!", False),
     ("Their address is: 123 Main Street, Anytown, AZ 85258-0001.", True),
     ("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.", False),
     ])
def test_check_zip_code(test_string, check_result):
    assert check_zip_code(test_string) is check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("One", False),
     ("123  Ready Set GO", True),
     ("username user_01", True),
     ("shopping_list: milk, bread, eggs.", False),
     ])
def test_check_character_groups(test_string, check_result):
    assert check_character_groups(test_string) is check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("Is this is a sentence?", True),
     ("is this is a sentence?", False),
     ("Hello", False),
     ("1-2-3-GO!", False),
     ("A star is born.", True),
     ])
def test_check_sentence(test_string, check_result):
    assert check_sentence(test_string) is check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("gmail.com", True),
     ("www@google", False),
     ("www.Coursera.org", True),
     ("web-address.com/homepage", False),
     ("My_Favorite-Blog.US", True),
     ("www.chicken/egg.com", False)
     ])
def test_check_web_address(test_string, check_result):
    assert check_web_address(test_string) is check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("12:45pm", True),
     ("9:59 AM", True),
     ("6:60am", False),
     ("five o'clock", False),
     ])
def test_check_time(test_string, check_result):
    assert check_time(test_string) is check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [('Kennedy, John F.', 'John F. Kennedy'),
     ('My perfect name', 'My perfect name'),
     ('Ford Prefect', 'Ford Prefect'),
     ('Picard, Jean-Luc', 'Jean-Luc Picard'),
     ('Heathcote-Drummond-Willoughby, Jane', 'Jane Heathcote-Drummond-Willoughby'),
     ])
def test_rearrange_name(test_string, check_result):
    assert rearrange_name(test_string) == check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("I like to drink coffee in the morning.", ['morning']),
     ("I also have a taste for hot chocolate in the afternoon.", ['chocolate', 'afternoon']),
     ("I never drink tea late at night.", []),
     ])
def test_long_words(test_string, check_result):
    assert long_words(test_string) == check_result


@pytest.mark.parametrize(
    'test_string, check_result',
    [("My number is 212-345-9999.", "My number is (212) 345-9999."),
     ("Please call 888-555-1234", "Please call (888) 555-1234"),
     ("123-123-12345", "123-123-12345"),
     ("Phone number of Buckingham Palace is +44 303 123 7300", "Phone number of Buckingham Palace is +44 303 123 7300"),
     ])
def test_convert_phone_number(test_string, check_result):
    assert convert_phone_number(test_string) == check_result
