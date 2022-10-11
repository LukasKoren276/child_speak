from .filehandling import Files
from .speakers import ISpeaker

class HumanTranslator:
    def __init__(self, speaker):
        self.speaker = speaker
        
    @property
    def speaker(self):
        return self.__speaker
    
    @speaker.setter
    def speaker(self, spkr):
        if not issubclass(type(spkr), ISpeaker):
            raise TypeError('Not a valid type. Speaker has to be an instance inherited from ISpeaker.')
        self.__speaker = spkr
              
    def _translate_words(self, words):
        for word in words:
            yield word, self.speaker.say(word)
        
    def _get_pairs(self, path):
        if path.endswith('json'):
            words = Files.load_json(path)
        else:
            try:
                words = Files.open_file(path)
                yield from self._translate_words(words)
            except UnicodeDecodeError:
                print('Unable to open such file.')
        
    def translate(self, path):   
        dct = {}
        for original, translation in self._get_pairs(path):
            dct[original] = translation
        return dct    
    