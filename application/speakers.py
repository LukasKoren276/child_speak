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
             
    def _starts_with_vowel(self, given_word):
        return given_word[0] in type(self)._vowels

    def _ends_with_consonant(self, word):
        return word[-1] in type(self)._consonants

    def _get_consonants(self, word):
        consonant_list = []
        for letter in word:
            if letter in type(self)._consonants:
                consonant_list.append(letter)
        return consonant_list

    def _replace_aftergoing_consonants(self, word, consonant):
        for letter in word:
            if letter in type(self)._consonants:
                word = word.replace(letter, consonant)
        return word

    def _replace_consecutive_vowels(self, word):
        new_str = []
        counter = 0
        for n, letter in enumerate(word):
            if letter in type(self)._consonants:
                new_str.append(letter)
                counter = 0
            else:
                new_str.append(letter)
                counter += 1
                if counter > 1:
                    new_str.pop(-2)
                    counter = 1
        return new_str

    def _replace_same_consecutive(self, word):
        last_letter = ''
        new_str = []
        for letter in word:
            if letter != last_letter:
                new_str.append(letter)
                last_letter = letter
        return ''.join(new_str)

    def say(self, given_word):
        if self._starts_with_vowel(given_word):
            word = self._get_consonants(given_word)[0] + given_word
        else: 
            word = given_word
        word = self._replace_aftergoing_consonants(word, word[0])
        word = self._replace_consecutive_vowels(word)
        word = self._replace_same_consecutive(word)
        if self._ends_with_consonant(word):
            return word[:-1]
        return word

