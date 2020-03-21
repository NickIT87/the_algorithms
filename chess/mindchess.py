import nltk

#nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - word tokenizers ... sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, Eng.lang.
# lexicon - words and their means
# investor-speak ... regular english-speak
# investor-speak 'bull' = someone who is positive about the market
# english-speak 'bull' = scary animal you dont want running @ you

example_text = ''' Sed ut perspiciatis unde omnis iste natus error sit 
voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa 
quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt 
explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit 
aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi 
nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, 
consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut 
labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, 
quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid 
ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea 
voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem 
eum fugiat quo voluptas nulla pariatur?
'''

print(sent_tokenize(example_text))

print(word_tokenize(example_text))