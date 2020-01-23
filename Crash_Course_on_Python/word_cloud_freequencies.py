from collections import Counter
from typing import Dict

def calculate_frequencies(file_contents: str) -> Dict[str, int]:
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE

    # Remove punctuation:
    punctuation_filter = str.maketrans('', '', punctuations)  # This will be faster than str.translate(None, punctuations)
    clean_string = file_contents.translate(punctuation_filter)

    # List words in lowercase to eliminate differently cased duplicates.
    words = clean_string.lower().split()

    # Create dict of word: count for words in text, given word is all text (no numbers) and is an 'interesting word'.
    frequencies = {word: count for word, count in Counter(words).items()
                   if word.isalpha() and word not in uninteresting_words}

    return frequencies
from pprint import pprint
pprint(calculate_frequencies(file_contents))