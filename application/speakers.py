from abc import ABCMeta, abstractmethod


class ISpeaker(metaclass=ABCMeta):
    
    @abstractmethod
    def say(self, given_word):
        'speaker says some given word in is language. Implementation follow, returns string.'


class ChildSpeaker(ISpeaker):
    """ A class that generates a word from a given word according to set rules"""
    
    _all_letters = 'abcdefghijklmnopqrstuvwxyz'
    _vowels = 'aeiouy'
    _consonants = 'bcdfghjklmnpqrstvwxz'    # tady nelze použít ''.join([letter for letter in all_letters if letter not in vowels])
   
    def _get_first_consonant(self, word):
        for letter in word:
            if letter in type(self)._consonants:
                return letter

    def say(self, word):
        first_consonant = self._get_first_consonant(word)
        if word[0] in type(self)._vowels:
            word = first_consonant + word
        new_word = []
        consonant_counter = 0
        vowel_counter = 0
        for letter in word:
            if letter in type(self)._consonants:
                vowel_counter = 0
                if consonant_counter == 0:
                    new_word.append(first_consonant)
                    consonant_counter += 1
            else:
                consonant_counter = 0
                vowel_counter += 1
                if vowel_counter > 1:
                    new_word = new_word[:-1]
                new_word.append(letter)
        if new_word[-1] in type(self)._consonants:
            new_word = new_word[:-1]
        return ''.join(new_word)
