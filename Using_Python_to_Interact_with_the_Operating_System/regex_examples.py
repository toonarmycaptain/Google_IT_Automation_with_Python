import re

from typing import List


def check_zip_code(text: str) -> bool:
    """
    Check if the text passed includes a possible U.S. zip code, formatted as
    follows: exactly 5 digits, and sometimes, but not always, followed by a
    dash with 4 more digits. The zip code needs to be preceded by at least one
    space, and cannot be at the start of the text.

    :param text: str
    :return: bool
    """
    result = re.search(r" \d{5}(-\d{4})?", text)
    return result is not None


def check_character_groups(text: str) -> bool:
    """
    Check if the text passed has at least 2 groups of alphanumeric characters
    (including letters, numbers, and underscores) separated by one or more
    whitespace characters.

    :param text: str
    :return: bool
    """
    result = re.search(r"\w+\s\w+", text)
    return result is not None


def check_sentence(text: str) -> bool:
    """
    Check if the text passed looks like a standard sentence, meaning that it
    starts with an uppercase letter, followed by at least some lowercase
    letters or a space, and ends with a period, question mark, or exclamation
    point.

    :param text: str
    :return: bool
    """
    result = re.search(r"^[A-Z][a-z ]*[\.\?\!]$", text)
    return result is not None


def check_web_address(text: str) -> bool:
    """
    Checks if the text passed qualifies as a top-level web address, meaning
    that it contains alphanumeric characters (which includes letters, numbers,
    and underscores), as well as periods, dashes, and a plus sign, followed by
    a period and a character-only top-level domain such as ".com", ".info",
    ".edu", etc.

    :param text: str
    :return: bool
    """
    pattern = r"^([a-zA-Z]{3}\.)?([a-zA-Z0-9_\.\-\+]+)([a-zA-Z])$"
    result = re.search(pattern, text)
    return result is not None


def check_time(text: str) -> bool:
    """
    Checks for the time format of a 12-hour clock, as follows: the hour is
    between 1 and 12, with no leading zero, followed by a colon, then minutes
    between 00 and 59, then an optional space, and then AM or PM, in upper or
    lower case.

    :param text: str
    :return: bool
    """
    pattern = "^([1-9]|1[0-2]):([0-5][0-9]) ?(am|AM|pm|PM)?$"
    result = re.search(pattern, text)
    return result is not None


def rearrange_name(name: str) -> str:
    """
    Rearranges a name that begins with surname and a comma to read with the
    surname last, accounting for middle names, middle initials, and double
    surnames.

    :param name: str
    :return: str
    """
    result = re.search(r"^([\w-]*), ([\w -]*\.?)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"


def long_words(text: str) -> List[str]:
    """
    Returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

    :param text: str
    :return: List[str]
    """
    pattern = r'\b(\w{7,})'
    result = re.findall(pattern, text)
    return result


def convert_phone_number(phone: str) -> str:
    """
    Checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a
    dash, 3 more digits followed by a dash, and 4 digits), and converts it to a
    more formal format that looks like this: (XXX) XXX-XXXX.

    :param phone: str
    :return: str
    """
    result = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', phone)
    return result
