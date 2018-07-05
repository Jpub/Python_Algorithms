import random
import string

alphabet = string.ascii_lowercase

random_word = alphabet[random.randrange(len(alphabet))] +    \
              alphabet[random.randrange(len(alphabet))] +    \
              alphabet[random.randrange(len(alphabet))] +    \
              alphabet[random.randrange(len(alphabet))] +    \
              alphabet[random.randrange(len(alphabet))]

print(random_word)
