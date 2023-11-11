import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def get_tense(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    tense_mapping = {
        'VB': 'present',   # Verb, base form
        'VBD': 'past',      # Verb, past tense
        'VBG': 'present',   # Verb, gerund/present participle
        'VBN': 'past',      # Verb, past participle
        'VBP': 'present',   # Verb, non-3rd person singular present
        'VBZ': 'present',   # Verb, 3rd person singular present
        'MD': 'future',     # Modal verb indicating future tense
    }

    # Add more mappings for additional tenses if needed
    # 'VBG': 'present_continuous', etc.

    tense = None

    for word, pos in tagged_words:
        if pos in tense_mapping:
            tense = tense_mapping[pos]
            break

    return tense

# Example usage
sentence_future = "I will be eating an apple."
sentence_present = "I eat an apple."
tense = get_tense(sentence_future)
print(f"The tense of the sentence is: {tense}")
