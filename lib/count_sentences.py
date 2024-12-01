#!/usr/bin/env python3
import re

class MyString:
  
    def __init__(self,value=""):
      pass
      self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        self._value = val
    def is_sentence(self):
       pass
       return self.value.endswith(".")
    def is_question(self):
       pass
       return self.value.endswith("?")
    def is_exclamation(self):
       return self.value.endswith("!")
    
    def count_sentences(self):
      if not isinstance(self.value, str):
        return 0
    
      
      sentences = re.split(r'[.!?]', self.value)
    
   
      sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
      return len(sentences)

  
        