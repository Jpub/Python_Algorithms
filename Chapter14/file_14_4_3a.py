import random
import string

alphabet = string.ascii_lowercase

random_word = alphabet[random.randrange(26)] +    \
              alphabet[random.randrange(26)] +    \
              alphabet[random.randrange(26)] +    \
              alphabet[random.randrange(26)] +    \
              alphabet[random.randrange(26)]

print(random_word)
